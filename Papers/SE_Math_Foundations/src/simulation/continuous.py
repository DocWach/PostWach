"""Continuous-time simulation via ODE integration."""

import numpy as np
from scipy.integrate import solve_ivp


def simulate_continuous(system, x0, t_span, input_fn, t_eval=None, method='RK45'):
    """Simulate a continuous-time system using scipy solve_ivp.

    Parameters
    ----------
    system : ContinuousSystem
        The system model to simulate.
    x0 : array_like
        Initial state vector.
    t_span : tuple
        (t_start, t_end).
    input_fn : callable
        Function u(t) returning input vector at time t.
    t_eval : array_like, optional
        Times at which to store the solution.
    method : str
        Integration method ('RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA').

    Returns
    -------
    result : dict
        Keys: 't' (times), 'x' (states), 'y' (outputs), 'u' (inputs).
    """
    x0 = np.atleast_1d(np.array(x0, dtype=float))

    def rhs(t, x):
        u = np.atleast_1d(np.array(input_fn(t), dtype=float))
        return system.state_derivative(t, x, u)

    sol = solve_ivp(rhs, t_span, x0, method=method, t_eval=t_eval,
                    rtol=1e-10, atol=1e-12)

    t = sol.t
    x = sol.y.T  # shape (n_times, n_states)
    u = np.array([np.atleast_1d(input_fn(ti)) for ti in t])
    y = np.array([system.output(xi, ui) for xi, ui in zip(x, u)])

    return {'t': t, 'x': x, 'y': y, 'u': u}
