"""Side-by-side simulation and metric computation for system pairs."""

import numpy as np
from .continuous import simulate_continuous


def compare_continuous(system_a, system_b, x0_a, x0_b, input_fn, t_span,
                       t_eval=None, variable_map=None):
    """Simulate two systems and compare their trajectories.

    Parameters
    ----------
    system_a, system_b : ContinuousSystem
        Two systems to compare.
    x0_a, x0_b : array_like
        Initial states (should be corresponding under variable mapping).
    input_fn : callable
        Input function u(t). Applied to both systems.
    t_span : tuple
        (t_start, t_end).
    t_eval : array_like, optional
        Evaluation times.
    variable_map : dict, optional
        Mapping from system_a output indices to system_b output indices.
        Default: identity (compare output i to output i).

    Returns
    -------
    result : dict
        Keys: 'result_a', 'result_b' (simulation results),
              'max_output_error', 'rms_output_error', 'trajectory_distance'.
    """
    res_a = simulate_continuous(system_a, x0_a, t_span, input_fn, t_eval)
    res_b = simulate_continuous(system_b, x0_b, t_span, input_fn, t_eval)

    # Interpolate to common time grid if needed
    t_common = res_a['t'] if t_eval is not None else res_a['t']
    y_a = res_a['y']
    y_b = res_b['y']

    # Handle potentially different time grids
    if len(y_a) != len(y_b) or not np.allclose(res_a['t'], res_b['t']):
        from scipy.interpolate import interp1d
        t_common = np.union1d(res_a['t'], res_b['t'])
        interp_a = interp1d(res_a['t'], y_a, axis=0, fill_value='extrapolate')
        interp_b = interp1d(res_b['t'], y_b, axis=0, fill_value='extrapolate')
        y_a = interp_a(t_common)
        y_b = interp_b(t_common)

    # Compute error metrics
    error = np.abs(y_a - y_b)
    max_error = np.max(error)
    rms_error = np.sqrt(np.mean(error**2))

    # Trajectory distance (L2 norm of output difference over time)
    dt = np.diff(t_common)
    mid_error = 0.5 * (error[:-1] + error[1:])
    trajectory_dist = np.sqrt(np.sum(mid_error**2 * dt[:, np.newaxis]))

    return {
        'result_a': res_a,
        'result_b': res_b,
        't_common': t_common,
        'y_a': y_a,
        'y_b': y_b,
        'max_output_error': max_error,
        'rms_output_error': rms_error,
        'trajectory_distance': trajectory_dist,
    }
