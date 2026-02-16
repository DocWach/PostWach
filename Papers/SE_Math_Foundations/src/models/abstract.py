"""Abstract base classes for state-space system models."""

import numpy as np
from abc import ABC, abstractmethod


class ContinuousSystem(ABC):
    """Continuous-time state-space system: dx/dt = f(x,u), y = g(x,u)."""

    @abstractmethod
    def state_derivative(self, t, x, u):
        """Compute dx/dt given state x and input u."""
        ...

    @abstractmethod
    def output(self, x, u):
        """Compute output y given state x and input u."""
        ...

    @property
    @abstractmethod
    def state_names(self):
        """Names of state variables."""
        ...

    @property
    @abstractmethod
    def input_names(self):
        """Names of input variables."""
        ...

    @property
    @abstractmethod
    def output_names(self):
        """Names of output variables."""
        ...

    @property
    def n_states(self):
        return len(self.state_names)

    @property
    def n_inputs(self):
        return len(self.input_names)

    @property
    def n_outputs(self):
        return len(self.output_names)


class LinearSystem(ContinuousSystem):
    """Linear time-invariant system: dx/dt = Ax + Bu, y = Cx + Du."""

    def __init__(self, A, B, C, D, state_names_list, input_names_list, output_names_list):
        self.A = np.atleast_2d(np.array(A, dtype=float))
        self.B = np.atleast_2d(np.array(B, dtype=float))
        self.C = np.atleast_2d(np.array(C, dtype=float))
        self.D = np.atleast_2d(np.array(D, dtype=float))
        self._state_names = list(state_names_list)
        self._input_names = list(input_names_list)
        self._output_names = list(output_names_list)

    def state_derivative(self, t, x, u):
        x = np.atleast_1d(np.array(x, dtype=float))
        u = np.atleast_1d(np.array(u, dtype=float))
        return self.A @ x + self.B @ u

    def output(self, x, u):
        x = np.atleast_1d(np.array(x, dtype=float))
        u = np.atleast_1d(np.array(u, dtype=float))
        return self.C @ x + self.D @ u

    @property
    def state_names(self):
        return self._state_names

    @property
    def input_names(self):
        return self._input_names

    @property
    def output_names(self):
        return self._output_names

    def transfer_function(self, s):
        """Evaluate transfer function H(s) = C(sI - A)^{-1}B + D."""
        n = self.A.shape[0]
        return self.C @ np.linalg.solve(s * np.eye(n) - self.A, self.B) + self.D
