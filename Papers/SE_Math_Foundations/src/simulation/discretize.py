"""Discretization methods for converting continuous to discrete systems."""

import numpy as np
from scipy.linalg import expm


def euler_discretize(A, B, dt):
    """Forward Euler: A_d = I + A*dt, B_d = B*dt. O(dt) error."""
    n = A.shape[0]
    A_d = np.eye(n) + A * dt
    B_d = B * dt
    return A_d, B_d


def rk4_discretize(A, B, dt):
    """RK4-based discretization for linear systems. O(dt^4) error.

    Uses the matrix exponential series truncated at 4th order.
    """
    n = A.shape[0]
    I = np.eye(n)
    A2 = A @ A
    A3 = A2 @ A
    A4 = A3 @ A
    A_d = I + A * dt + A2 * (dt**2 / 2) + A3 * (dt**3 / 6) + A4 * (dt**4 / 24)
    B_int = (I * dt + A * (dt**2 / 2) + A2 * (dt**3 / 6) + A3 * (dt**4 / 24))
    B_d = B_int @ B
    return A_d, B_d


def exact_discretize(A, B, dt):
    """Exact discretization via matrix exponential. Preserves isomorphism for linear systems.

    A_d = expm(A*dt)
    B_d = A^{-1}(A_d - I)B  (or integral form if A is singular)
    """
    n = A.shape[0]
    A_d = expm(A * dt)
    try:
        B_d = np.linalg.solve(A, (A_d - np.eye(n)) @ B)
    except np.linalg.LinAlgError:
        # A is singular; use numerical integration
        from scipy.integrate import quad_vec
        def integrand(tau):
            return (expm(A * tau) @ B).flatten()
        result, _ = quad_vec(integrand, 0, dt)
        B_d = result.reshape(B.shape)
    return A_d, B_d


def simulate_discrete(A_d, B_d, C, D, x0, u_sequence):
    """Simulate a discrete-time linear system (Moore machine).

    x[k+1] = A_d @ x[k] + B_d @ u[k]
    y[k] = C @ x[k] + D @ u[k]

    Parameters
    ----------
    A_d, B_d, C, D : ndarray
        Discrete system matrices.
    x0 : array_like
        Initial state.
    u_sequence : ndarray
        Input sequence, shape (n_steps, n_inputs).

    Returns
    -------
    x_traj : ndarray, shape (n_steps+1, n_states)
    y_traj : ndarray, shape (n_steps+1, n_outputs)
    """
    x0 = np.atleast_1d(np.array(x0, dtype=float))
    n_steps = len(u_sequence)
    n_states = len(x0)
    n_outputs = C.shape[0]

    x_traj = np.zeros((n_steps + 1, n_states))
    y_traj = np.zeros((n_steps + 1, n_outputs))
    x_traj[0] = x0
    u0 = np.atleast_1d(u_sequence[0])
    y_traj[0] = (C @ x0 + D @ u0).flatten()

    for k in range(n_steps):
        u_k = np.atleast_1d(u_sequence[k])
        x_traj[k + 1] = (A_d @ x_traj[k] + B_d @ u_k).flatten()
        y_traj[k + 1] = (C @ x_traj[k + 1] + D @ u_k).flatten()

    return x_traj, y_traj
