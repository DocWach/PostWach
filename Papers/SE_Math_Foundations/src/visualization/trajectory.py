"""Trajectory visualization for comparing isomorphic system responses."""

import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory_comparison(result, title=None, labels=None, save_path=None):
    """Plot overlay of two system trajectories from a comparison result.

    Parameters
    ----------
    result : dict
        Output from compare_continuous().
    title : str, optional
        Plot title.
    labels : tuple of str, optional
        Labels for (system_a, system_b). Default: ('System A', 'System B').
    save_path : str, optional
        If provided, save figure to this path.
    """
    if labels is None:
        labels = ('System A', 'System B')

    t_a = result['result_a']['t']
    t_b = result['result_b']['t']
    y_a = result['result_a']['y']
    y_b = result['result_b']['y']

    n_outputs = y_a.shape[1] if y_a.ndim > 1 else 1

    fig, axes = plt.subplots(n_outputs + 1, 1, figsize=(10, 3 * (n_outputs + 1)),
                             sharex=True)
    if n_outputs == 1:
        axes = [axes] if not hasattr(axes, '__len__') else list(axes)

    for i in range(n_outputs):
        ax = axes[i]
        ya_i = y_a[:, i] if y_a.ndim > 1 else y_a
        yb_i = y_b[:, i] if y_b.ndim > 1 else y_b
        ax.plot(t_a, ya_i, 'b-', linewidth=2, label=labels[0])
        ax.plot(t_b, yb_i, 'r--', linewidth=2, label=labels[1])
        ax.set_ylabel(f'Output {i + 1}')
        ax.legend()
        ax.grid(True, alpha=0.3)

    # Error plot
    ax_err = axes[-1]
    t_common = result.get('t_common', t_a)
    y_a_common = result.get('y_a', y_a)
    y_b_common = result.get('y_b', y_b)
    error = np.abs(y_a_common - y_b_common)
    if error.ndim > 1:
        error = np.max(error, axis=1)
    ax_err.semilogy(t_common, error + 1e-16, 'k-', linewidth=1)
    ax_err.set_ylabel('|Error|')
    ax_err.set_xlabel('Time')
    ax_err.grid(True, alpha=0.3)

    if title:
        fig.suptitle(title, fontsize=14)

    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')

    return fig, axes


def plot_discretization_degradation(dt_values, errors_by_method, title=None,
                                     save_path=None):
    """Plot morphism distance D vs discretization step size for different methods.

    Parameters
    ----------
    dt_values : array_like
        Step sizes tested.
    errors_by_method : dict
        {method_name: array of errors corresponding to dt_values}.
    title : str, optional
        Plot title.
    save_path : str, optional
        If provided, save figure to this path.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    markers = ['o', 's', '^', 'D', 'v']
    for idx, (method, errors) in enumerate(errors_by_method.items()):
        marker = markers[idx % len(markers)]
        ax.loglog(dt_values, errors + 1e-16, f'-{marker}', linewidth=2,
                  markersize=8, label=method)

    # Reference slopes
    dt_ref = np.array(dt_values)
    ax.loglog(dt_ref, dt_ref * errors_by_method.get('Euler', [1])[0] / dt_ref[0],
              'k:', alpha=0.5, label='O(dt)')
    ax.loglog(dt_ref, dt_ref**4 * 1e-2, 'k--', alpha=0.5, label='O(dt^4)')

    ax.set_xlabel('Step size (dt)', fontsize=12)
    ax.set_ylabel('Morphism distance D', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')

    if title:
        ax.set_title(title, fontsize=14)

    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')

    return fig, ax
