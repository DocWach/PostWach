@echo off
REM Claude-Flow local wrapper
REM This script ensures claude-flow runs from your project directory

setlocal enabledelayedexpansion

set PROJECT_DIR=%CD%
set PWD=%PROJECT_DIR%
set CLAUDE_WORKING_DIR=%PROJECT_DIR%

REM Try to find claude-flow binary
REM Check common locations for npm/npx installations

REM 1. Local node_modules (npm install claude-flow)
if exist "%PROJECT_DIR%\node_modules\.bin\claude-flow.cmd" (
  cd /d "%PROJECT_DIR%"
  "%PROJECT_DIR%\node_modules\.bin\claude-flow.cmd" %*
  exit /b !ERRORLEVEL!
)

REM 2. Parent directory node_modules (monorepo setup)
if exist "%PROJECT_DIR%\..\node_modules\.bin\claude-flow.cmd" (
  cd /d "%PROJECT_DIR%"
  "%PROJECT_DIR%\..\node_modules\.bin\claude-flow.cmd" %*
  exit /b !ERRORLEVEL!
)

REM 3. Global installation (find one that isn't THIS script)
for /f "usebackq tokens=*" %%i in (`where claude-flow`) do (
  set "EXE_PATH=%%i"
  if /i "!EXE_PATH!" neq "%~f0" (
    if /i "!EXE_PATH!" neq "%~dp0claude-flow" (
      cd /d "%PROJECT_DIR%"
      "!EXE_PATH!" %*
      exit /b !ERRORLEVEL!
    )
  )
)

REM 4. Fallback to npx (will download if needed)
cd /d "%PROJECT_DIR%"
npx claude-flow@latest %*
