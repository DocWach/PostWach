"""Mechanical system models (translational and rotational)."""

import numpy as np
from .abstract import LinearSystem


class MassSpringDamper(LinearSystem):
    """Translational mass-spring-damper: M*x'' + B*x' + K*x = F(t).

    State: [position x, velocity v]
    Input: [force F]
    Output: [position x]
    """

    def __init__(self, M, B, K):
        self.M = float(M)
        self.B_damp = float(B)
        self.K = float(K)
        A = np.array([[0, 1],
                       [-K / M, -B / M]])
        B_mat = np.array([[0],
                           [1 / M]])
        C = np.array([[1, 0]])
        D = np.array([[0]])
        super().__init__(A, B_mat, C, D,
                         ['position', 'velocity'],
                         ['force'],
                         ['position'])

    def hamiltonian(self, x):
        """Total energy: H = 0.5*K*x^2 + 0.5*M*v^2."""
        pos, vel = x[0], x[1]
        return 0.5 * self.K * pos**2 + 0.5 * self.M * vel**2


class RotationalMSD(LinearSystem):
    """Rotational mass-spring-damper: J*theta'' + B_r*theta' + K_r*theta = tau(t).

    State: [angle theta, angular velocity omega]
    Input: [torque tau]
    Output: [angle theta]
    """

    def __init__(self, J, B_r, K_r):
        self.J = float(J)
        self.B_r = float(B_r)
        self.K_r = float(K_r)
        A = np.array([[0, 1],
                       [-K_r / J, -B_r / J]])
        B_mat = np.array([[0],
                           [1 / J]])
        C = np.array([[1, 0]])
        D = np.array([[0]])
        super().__init__(A, B_mat, C, D,
                         ['angle', 'angular_velocity'],
                         ['torque'],
                         ['angle'])

    def hamiltonian(self, x):
        """Total energy: H = 0.5*K_r*theta^2 + 0.5*J*omega^2."""
        theta, omega = x[0], x[1]
        return 0.5 * self.K_r * theta**2 + 0.5 * self.J * omega**2
