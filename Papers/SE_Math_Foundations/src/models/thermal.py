"""Thermal system models."""

import numpy as np
from .abstract import LinearSystem


class ThermalRC(LinearSystem):
    """Thermal RC system: R_th*C_th*T' + T = T_source(t).

    First-order only (no thermal inertance / no inductor analog).

    State: [temperature T]
    Input: [source temperature T_source]
    Output: [temperature T]
    """

    def __init__(self, R_th, C_th):
        self.R_th = float(R_th)
        self.C_th = float(C_th)
        tau = R_th * C_th
        A = np.array([[-1 / tau]])
        B_mat = np.array([[1 / tau]])
        C_out = np.array([[1]])
        D = np.array([[0]])
        super().__init__(A, B_mat, C_out, D,
                         ['temperature'],
                         ['source_temperature'],
                         ['temperature'])

    def thermal_energy(self, x, T_ref=0.0):
        """Stored thermal energy: E = C_th * (T - T_ref)."""
        return self.C_th * (x[0] - T_ref)
