"""ORCiD Public API OAuth helper.

P1 of the PostWach ORCiD push-only sync workflow. Performs the 3-legged OAuth
authorization-code flow against ORCiD's Public API, captures the access token,
caches it, and reads the public record as a smoke test.

No write operations are performed. Token is requested with all scopes the
later phases (P3-P5) will need so authorization happens once.

Usage:
    python scripts/orcid/auth.py --smoke-test

Reads credentials from ~/.config/postwach/orcid.env (gitignored, user-home).
Writes token cache to scripts/orcid/state/token_cache.json (gitignored).
"""

import argparse
import functools
import http.server
import json
import os
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

import requests

# Force unbuffered stdout/stderr so background runners see progress in real time.
print = functools.partial(print, flush=True)  # noqa: A001

ENV_FILE = Path.home() / ".config" / "postwach" / "orcid.env"
STATE_DIR = Path(__file__).resolve().parent / "state"
TOKEN_CACHE = STATE_DIR / "token_cache.json"

SCOPES = "/authenticate"  # Public API tier supports /authenticate only.


def env_endpoints(environment):
    if environment == "sandbox":
        return ("https://sandbox.orcid.org", "https://api.sandbox.orcid.org")
    return ("https://orcid.org", "https://pub.orcid.org")


def load_env():
    if not ENV_FILE.exists():
        sys.exit(
            f"Missing env file: {ENV_FILE}\n"
            "Create it with: ORCID_CLIENT_ID, ORCID_CLIENT_SECRET, "
            "ORCID_REDIRECT_URI, ORCID_ENVIRONMENT, ORCID_RECORD_HOLDER."
        )
    env = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip().strip('"').strip("'")
    required = [
        "ORCID_CLIENT_ID",
        "ORCID_CLIENT_SECRET",
        "ORCID_REDIRECT_URI",
        "ORCID_ENVIRONMENT",
        "ORCID_RECORD_HOLDER",
    ]
    missing = [k for k in required if not env.get(k)]
    if missing:
        sys.exit(f"Missing env keys in {ENV_FILE}: {missing}")
    return env


def load_token_cache():
    if not TOKEN_CACHE.exists():
        return None
    try:
        cache = json.loads(TOKEN_CACHE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if cache.get("expires_at", 0) < time.time() + 300:
        return None
    return cache


def save_token_cache(token):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    expires_at = time.time() + token.get("expires_in", 0)
    cache = {**token, "expires_at": expires_at}
    TOKEN_CACHE.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    try:
        os.chmod(TOKEN_CACHE, 0o600)
    except OSError:
        pass


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    captured = None
    protocol_version = "HTTP/1.0"  # one-shot connections; no keep-alive ambiguity

    def _respond(self, status, body_bytes, content_type="text/html; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body_bytes)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body_bytes)
        try:
            self.wfile.flush()
        except Exception:
            pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        print(f"  [callback] GET {self.path}")
        if "code" in params:
            CallbackHandler.captured = {"code": params["code"][0]}
            body = (
                b"<html><body style='font-family:sans-serif;padding:2em'>"
                b"<h2>ORCiD authorization received.</h2>"
                b"<p>You can close this tab and return to the terminal.</p>"
                b"</body></html>"
            )
            self._respond(200, body)
        elif "error" in params:
            CallbackHandler.captured = {"error": params.get("error", ["?"])[0]}
            self._respond(400, b"<h2>ORCiD returned an error. See terminal.</h2>")
        else:
            # Likely a favicon or probe; respond cheaply, do NOT mark captured.
            self._respond(404, b"not the callback we expected")

    def log_message(self, fmt, *args):
        # Surface short access lines so we can see what Edge is actually hitting.
        print(f"  [http] {self.address_string()} - {fmt % args}")


def run_oauth_flow(env):
    auth_base, _ = env_endpoints(env["ORCID_ENVIRONMENT"])
    redirect_uri = env["ORCID_REDIRECT_URI"]

    parsed = urllib.parse.urlparse(redirect_uri)
    if parsed.hostname not in ("127.0.0.1", "localhost"):
        sys.exit(
            f"ORCID_REDIRECT_URI must be a localhost callback "
            f"(got {redirect_uri}). See docs/orcid-workflow.md."
        )
    port = parsed.port or 8765
    path = parsed.path or "/callback"

    params = {
        "client_id": env["ORCID_CLIENT_ID"],
        "response_type": "code",
        "scope": SCOPES,
        "redirect_uri": redirect_uri,
    }
    authorize_url = f"{auth_base}/oauth/authorize?{urllib.parse.urlencode(params, safe='/ ')}"

    print()
    print("Open this URL in a browser to authorize DocWach_ORCiD:")
    print(f"  {authorize_url}")
    print()
    # Launch Microsoft Edge directly (no cmd shell; cmd interprets & as command separator).
    edge_candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    edge_exe = next((p for p in edge_candidates if Path(p).exists()), None)
    if edge_exe:
        try:
            subprocess.Popen(
                [edge_exe, authorize_url],
                creationflags=getattr(subprocess, "DETACHED_PROCESS", 0),
            )
            print(f"Launched Microsoft Edge: {edge_exe}")
        except Exception as exc:
            print(f"Could not launch Edge ({exc}); copy the URL above into your browser.")
    else:
        print("Microsoft Edge executable not found in standard paths.")
        print("Copy the URL above into your browser manually.")

    server = http.server.HTTPServer(("127.0.0.1", port), CallbackHandler)
    print(f"Listening for ORCiD callback on http://127.0.0.1:{port}{path} ...")
    server.timeout = 300
    while CallbackHandler.captured is None:
        server.handle_request()

    if "error" in CallbackHandler.captured:
        sys.exit(f"OAuth error from ORCiD: {CallbackHandler.captured['error']}")
    code = CallbackHandler.captured["code"]
    print("Authorization code received. Exchanging for token ...")

    resp = requests.post(
        f"{auth_base}/oauth/token",
        headers={"Accept": "application/json"},
        data={
            "client_id": env["ORCID_CLIENT_ID"],
            "client_secret": env["ORCID_CLIENT_SECRET"],
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
        },
        timeout=30,
    )
    if resp.status_code >= 400:
        sys.exit(f"Token exchange failed: HTTP {resp.status_code}\n{resp.text}")
    token = resp.json()
    save_token_cache(token)
    print(f"Token cached at {TOKEN_CACHE}")
    return token


def get_token(env):
    cached = load_token_cache()
    if cached:
        print(f"Using cached token (expires in ~{(cached['expires_at']-time.time())/86400:.0f} days)")
        return cached
    print("No valid token cache; starting OAuth flow.")
    return run_oauth_flow(env)


def smoke_test_read(env, token):
    _, api_base = env_endpoints(env["ORCID_ENVIRONMENT"])
    orcid_id = env["ORCID_RECORD_HOLDER"]
    headers = {
        "Accept": "application/vnd.orcid+json",
        "Authorization": f"Bearer {token['access_token']}",
    }
    resp = requests.get(f"{api_base}/v3.0/{orcid_id}/record", headers=headers, timeout=30)
    if resp.status_code >= 400:
        sys.exit(f"Record read failed: HTTP {resp.status_code}\n{resp.text}")
    record = resp.json()

    person = record.get("person", {}) or {}
    name = person.get("name") or {}
    given = (name.get("given-names") or {}).get("value", "?")
    family = (name.get("family-name") or {}).get("value", "?")

    activities = record.get("activities-summary", {}) or {}
    works = (activities.get("works") or {}).get("group", [])
    employments = (activities.get("employments") or {}).get("affiliation-group", [])
    educations = (activities.get("educations") or {}).get("affiliation-group", [])
    distinctions = (activities.get("distinctions") or {}).get("affiliation-group", [])

    print()
    print(f"=== ORCiD smoke test: {orcid_id} ===")
    print(f"Name:              {given} {family}")
    print(f"Works:             {len(works)}")
    print(f"Employments:       {len(employments)}")
    print(f"Education:         {len(educations)}")
    print(f"Distinctions:      {len(distinctions)}")
    print(f"Token scope:       {token.get('scope')}")
    days = token.get("expires_in", 0) / 86400
    print(f"Token lifetime:    ~{days:.0f} days")
    print()
    print("P1 smoke test PASS. No writes performed.")


def main():
    parser = argparse.ArgumentParser(description="ORCiD OAuth + smoke-test (P1).")
    parser.add_argument("--smoke-test", action="store_true",
                        help="Run OAuth flow and read record summary (default).")
    parser.add_argument("--clear-cache", action="store_true",
                        help="Delete the cached token and exit.")
    args = parser.parse_args()

    if args.clear_cache:
        if TOKEN_CACHE.exists():
            TOKEN_CACHE.unlink()
            print(f"Removed {TOKEN_CACHE}")
        else:
            print(f"No cache to remove at {TOKEN_CACHE}")
        return

    env = load_env()
    token = get_token(env)
    smoke_test_read(env, token)


if __name__ == "__main__":
    main()
