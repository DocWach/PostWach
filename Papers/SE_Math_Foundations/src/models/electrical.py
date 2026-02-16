"""Electrical circuit models (series and parallel RLC)."""

import numpy as np
from .abstract import LinearSystem


class SeriesRLC(LinearSystem):
    """Series RLC circuit: L*q'' + R*q' + (1/C)*q = V(t).

    State: [charge q, current i]
    Input: [voltage V]
    Output: [charge q]
    """

    def __init__(self, L, R, C):
        self.L = float(L)
        self.R = float(R)
        self.C_cap = float(C)
        A = np.array([[0, 1],
                       [-1 / (L * C), -R / L]])
        B_mat = np.array([[0],
                           [1 / L]])
        C_out = np.array([[1, 0]])
        D = np.array([[0]])
        super().__init__(A, B_mat, C_out, D,
                         ['charge', 'current'],
                         ['voltage'],
                         ['charge'])

    @classmethod
    def from_mechanical(cls, M, B, K):
        """Create series RLC with parameters mapped from MSD (force-voltage)."""
        return cls(L=M, R=B, C=1.0 / K)

    def hamiltonian(self, x):
        """Total energy: H = 0.5*q^2/C + 0.5*L*i^2."""
        q, i = x[0], x[1]
        return 0.5 * q**2 / self.C_cap + 0.5 * self.L * i**2


class ParallelRLC(LinearSystem):
    """Parallel RLC circuit: C*v'' + (1/R)*v' + (1/L)*v = I(t).

    State: [flux linkage phi, voltage v]
    Input: [current I]
    Output: [flux linkage phi]
    """

    def __init__(self, L, R, C):
        self.L = float(L)
        self.R = float(R)
        self.C_cap = float(C)
        A = np.array([[0, 1],
                       [-1 / (L * C), -1 / (R * C)]])
        B_mat = np.array([[0],
                           [1 / C]])
        C_out = np.array([[1, 0]])
        D = np.array([[0]])
        super().__init__(A, B_mat, C_out, D,
                         ['flux_linkage', 'voltage'],
                         ['current'],
                         ['flux_linkage'])

    @classmethod
    def from_mechanical(cls, M, B, K):
        """Create parallel RLC with parameters mapped from MSD (force-current)."""
        return cls(L=1.0 / K, R=1.0 / B, C=M)

    def hamiltonian(self, x):
        """Total energy: H = 0.5*phi^2/L + 0.5*C*v^2."""
        phi, v = x[0], x[1]
        return 0.5 * phi**2 / self.L + 0.5 * self.C_cap * v**2
