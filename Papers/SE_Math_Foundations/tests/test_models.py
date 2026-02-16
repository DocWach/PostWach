"""Tests for system model implementations."""

import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.models.mechanical import MassSpringDamper, RotationalMSD
from src.models.electrical import SeriesRLC, ParallelRLC
from src.models.thermal import ThermalRC
from src.simulation.continuous import simulate_continuous


# --- Fixtures ---

@pytest.fixture
def msd():
    """Mass-spring-damper: M=1, B=0.5, K=2."""
    return MassSpringDamper(M=1.0, B=0.5, K=2.0)


@pytest.fixture
def rlc():
    """Series RLC mapped from MSD: L=1, R=0.5, C=0.5."""
    return SeriesRLC.from_mechanical(M=1.0, B=0.5, K=2.0)


@pytest.fixture
def thermal():
    """Thermal RC: R_th=1, C_th=1."""
    return ThermalRC(R_th=1.0, C_th=1.0)


# --- Model Construction Tests ---

class TestMassSpringDamper:
    def test_dimensions(self, msd):
        assert msd.n_states == 2
        assert msd.n_inputs == 1
        assert msd.n_outputs == 1

    def test_state_names(self, msd):
        assert msd.state_names == ['position', 'velocity']

    def test_A_matrix(self, msd):
        expected_A = np.array([[0, 1], [-2.0, -0.5]])
        np.testing.assert_array_almost_equal(msd.A, expected_A)

    def test_B_matrix(self, msd):
        expected_B = np.array([[0], [1.0]])
        np.testing.assert_array_almost_equal(msd.B, expected_B)

    def test_zero_state_derivative(self, msd):
        dx = msd.state_derivative(0, [0, 0], [0])
        np.testing.assert_array_almost_equal(dx, [0, 0])

    def test_forced_state_derivative(self, msd):
        # At x=[0,0] with F=1: dx = [0, 1/M] = [0, 1]
        dx = msd.state_derivative(0, [0, 0], [1])
        np.testing.assert_array_almost_equal(dx, [0, 1.0])

    def test_hamiltonian_at_rest(self, msd):
        assert msd.hamiltonian([0, 0]) == 0.0

    def test_hamiltonian_positive(self, msd):
        assert msd.hamiltonian([1, 1]) > 0


class TestSeriesRLC:
    def test_dimensions(self, rlc):
        assert rlc.n_states == 2
        assert rlc.n_inputs == 1
        assert rlc.n_outputs == 1

    def test_from_mechanical_mapping(self, rlc):
        assert rlc.L == 1.0
        assert rlc.R == 0.5
        assert rlc.C_cap == 0.5

    def test_A_matrix_matches_msd(self, msd, rlc):
        """The A matrices of isomorphic MSD and RLC should be identical."""
        np.testing.assert_array_almost_equal(msd.A, rlc.A)

    def test_B_matrix_matches_msd(self, msd, rlc):
        np.testing.assert_array_almost_equal(msd.B, rlc.B)


class TestParallelRLC:
    def test_from_mechanical(self):
        p = ParallelRLC.from_mechanical(M=1.0, B=0.5, K=2.0)
        assert p.L == 0.5
        assert p.R == 2.0
        assert p.C_cap == 1.0

    def test_dimensions(self):
        p = ParallelRLC(L=1, R=1, C=1)
        assert p.n_states == 2


class TestRotationalMSD:
    def test_structural_isomorphism_with_translational(self):
        """Rotational MSD with same numerical params has same A matrix as translational."""
        msd = MassSpringDamper(M=2.0, B=0.3, K=1.5)
        rot = RotationalMSD(J=2.0, B_r=0.3, K_r=1.5)
        np.testing.assert_array_almost_equal(msd.A, rot.A)
        np.testing.assert_array_almost_equal(msd.B, rot.B)


class TestThermalRC:
    def test_dimensions(self, thermal):
        assert thermal.n_states == 1
        assert thermal.n_inputs == 1
        assert thermal.n_outputs == 1

    def test_first_order(self, thermal):
        """Thermal is first-order (1 state), unlike 2nd-order MSD/RLC."""
        assert thermal.A.shape == (1, 1)


# --- Simulation Tests ---

class TestSimulation:
    def test_msd_step_response_decays(self, msd):
        """Underdamped MSD step response should oscillate and settle."""
        t_eval = np.linspace(0, 20, 500)
        result = simulate_continuous(
            msd, x0=[0, 0], t_span=(0, 20),
            input_fn=lambda t: [1.0], t_eval=t_eval
        )
        # Final value should approach F/K = 1/2 = 0.5
        final_pos = result['y'][-1, 0]
        assert abs(final_pos - 0.5) < 0.01

    def test_msd_free_response_energy_decreases(self, msd):
        """Energy should decrease monotonically for damped free response."""
        t_eval = np.linspace(0, 10, 200)
        result = simulate_continuous(
            msd, x0=[1, 0], t_span=(0, 10),
            input_fn=lambda t: [0.0], t_eval=t_eval
        )
        energies = [msd.hamiltonian(xi) for xi in result['x']]
        # Energy should be non-increasing (with numerical tolerance)
        for i in range(1, len(energies)):
            assert energies[i] <= energies[i - 1] + 1e-8

    def test_thermal_step_response(self, thermal):
        """Thermal RC step response: T -> T_source exponentially."""
        t_eval = np.linspace(0, 10, 200)
        result = simulate_continuous(
            thermal, x0=[0], t_span=(0, 10),
            input_fn=lambda t: [1.0], t_eval=t_eval
        )
        # Should approach T_source=1.0
        final_temp = result['y'][-1, 0]
        assert abs(final_temp - 1.0) < 0.01


# --- Transfer Function Tests ---

class TestTransferFunction:
    def test_msd_rlc_identical_tf(self, msd, rlc):
        """Isomorphic MSD and RLC should have identical transfer functions."""
        # Test at several frequencies
        for omega in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            s = 1j * omega
            H_msd = msd.transfer_function(s)
            H_rlc = rlc.transfer_function(s)
            np.testing.assert_array_almost_equal(H_msd, H_rlc)

    def test_tf_dc_gain(self, msd):
        """DC gain H(0) = -C * A^{-1} * B + D = 1/K for MSD."""
        # At s -> 0 (use small s to avoid singularity)
        H_dc = msd.transfer_function(1e-10)
        expected_dc = 1.0 / msd.K  # 1/2 = 0.5
        assert abs(H_dc[0, 0].real - expected_dc) < 1e-4
