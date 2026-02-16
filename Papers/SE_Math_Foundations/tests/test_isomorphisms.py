"""Tests verifying known isomorphisms produce D=0 for continuous models."""

import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.models.mechanical import MassSpringDamper, RotationalMSD
from src.models.electrical import SeriesRLC, ParallelRLC
from src.models.thermal import ThermalRC
from src.simulation.continuous import simulate_continuous
from src.simulation.comparison import compare_continuous
from src.simulation.discretize import (
    euler_discretize, rk4_discretize, exact_discretize, simulate_discrete
)


# --- Test Parameters ---
M, B_DAMP, K = 1.0, 0.5, 2.0
T_SPAN = (0, 10)
T_EVAL = np.linspace(0, 10, 1000)
X0 = [0, 0]
STEP_INPUT = lambda t: [1.0]
TOL_CONTINUOUS = 1e-8
TOL_EXACT_DISC = 1e-6


# --- I-1: MSD / Series RLC (force-voltage) ---

class TestI1_MSD_SeriesRLC:
    """Verify exact isomorphism between MSD and series RLC (force-voltage)."""

    @pytest.fixture
    def systems(self):
        msd = MassSpringDamper(M, B_DAMP, K)
        rlc = SeriesRLC.from_mechanical(M, B_DAMP, K)
        return msd, rlc

    def test_A_matrices_identical(self, systems):
        msd, rlc = systems
        np.testing.assert_array_almost_equal(msd.A, rlc.A)

    def test_B_matrices_identical(self, systems):
        msd, rlc = systems
        np.testing.assert_array_almost_equal(msd.B, rlc.B)

    def test_continuous_output_identical(self, systems):
        """D=0 for continuous-time simulation under variable mapping."""
        msd, rlc = systems
        result = compare_continuous(
            msd, rlc, X0, X0, STEP_INPUT, T_SPAN, t_eval=T_EVAL
        )
        assert result['max_output_error'] < TOL_CONTINUOUS

    def test_continuous_trajectory_distance_zero(self, systems):
        msd, rlc = systems
        result = compare_continuous(
            msd, rlc, X0, X0, STEP_INPUT, T_SPAN, t_eval=T_EVAL
        )
        assert result['trajectory_distance'] < TOL_CONTINUOUS

    def test_step_response_identical(self, systems):
        msd, rlc = systems
        res_msd = simulate_continuous(msd, X0, T_SPAN, STEP_INPUT, t_eval=T_EVAL)
        res_rlc = simulate_continuous(rlc, X0, T_SPAN, STEP_INPUT, t_eval=T_EVAL)
        np.testing.assert_allclose(res_msd['y'], res_rlc['y'], atol=TOL_CONTINUOUS)

    def test_impulse_response_identical(self, systems):
        msd, rlc = systems
        # Approximate impulse: short pulse
        impulse = lambda t: [100.0] if t < 0.01 else [0.0]
        res_msd = simulate_continuous(msd, X0, T_SPAN, impulse, t_eval=T_EVAL)
        res_rlc = simulate_continuous(rlc, X0, T_SPAN, impulse, t_eval=T_EVAL)
        np.testing.assert_allclose(res_msd['y'], res_rlc['y'], atol=TOL_CONTINUOUS)

    def test_sinusoidal_response_identical(self, systems):
        msd, rlc = systems
        sine_input = lambda t: [np.sin(2 * np.pi * t)]
        res_msd = simulate_continuous(msd, X0, T_SPAN, sine_input, t_eval=T_EVAL)
        res_rlc = simulate_continuous(rlc, X0, T_SPAN, sine_input, t_eval=T_EVAL)
        np.testing.assert_allclose(res_msd['y'], res_rlc['y'], atol=TOL_CONTINUOUS)

    def test_hamiltonian_identical(self, systems):
        """Energy functions should be identical under variable mapping."""
        msd, rlc = systems
        res_msd = simulate_continuous(msd, X0, T_SPAN, STEP_INPUT, t_eval=T_EVAL)
        for x_state in res_msd['x'][::50]:
            H_msd = msd.hamiltonian(x_state)
            H_rlc = rlc.hamiltonian(x_state)
            assert abs(H_msd - H_rlc) < TOL_CONTINUOUS


# --- I-3: Translational / Rotational ---

class TestI3_TranslationalRotational:
    """Verify exact isomorphism between translational and rotational MSD."""

    def test_continuous_output_identical(self):
        msd = MassSpringDamper(M, B_DAMP, K)
        rot = RotationalMSD(J=M, B_r=B_DAMP, K_r=K)
        result = compare_continuous(
            msd, rot, X0, X0, STEP_INPUT, T_SPAN, t_eval=T_EVAL
        )
        assert result['max_output_error'] < TOL_CONTINUOUS


# --- I-5: Electrical / Thermal (partial) ---

class TestI5_ElectricalThermal:
    """Verify PARTIAL isomorphism: RC circuit matches thermal RC, but full RLC does not."""

    def test_rc_thermal_match(self):
        """First-order RC and thermal RC with mapped params should match."""
        from src.models.abstract import LinearSystem
        # RC circuit: tau*V' + V = V_in  =>  A = [-1/tau], B = [1/tau]
        tau = 1.0
        rc = LinearSystem(
            A=[[-1 / tau]], B=[[1 / tau]], C=[[1]], D=[[0]],
            state_names_list=['voltage'], input_names_list=['source_voltage'],
            output_names_list=['voltage']
        )
        thermal = ThermalRC(R_th=1.0, C_th=1.0)  # tau = R*C = 1
        result = compare_continuous(
            rc, thermal, [0], [0], lambda t: [1.0], T_SPAN, t_eval=T_EVAL
        )
        assert result['max_output_error'] < TOL_CONTINUOUS

    def test_rlc_thermal_mismatch(self):
        """Full 2nd-order RLC does NOT match 1st-order thermal (different dimensions)."""
        rlc = SeriesRLC(L=1, R=1, C=1)
        thermal = ThermalRC(R_th=1.0, C_th=1.0)
        assert rlc.n_states != thermal.n_states


# --- Discretization Tests ---

class TestDiscretizationIsomorphismPreservation:
    """Test whether discretization preserves the MSD/RLC isomorphism."""

    @pytest.fixture
    def linear_systems(self):
        msd = MassSpringDamper(M, B_DAMP, K)
        rlc = SeriesRLC.from_mechanical(M, B_DAMP, K)
        return msd, rlc

    def test_exact_discretization_preserves_isomorphism(self, linear_systems):
        """Matrix exponential discretization should preserve D=0."""
        msd, rlc = linear_systems
        dt = 0.01
        A_d_msd, B_d_msd = exact_discretize(msd.A, msd.B, dt)
        A_d_rlc, B_d_rlc = exact_discretize(rlc.A, rlc.B, dt)
        np.testing.assert_allclose(A_d_msd, A_d_rlc, atol=TOL_EXACT_DISC)
        np.testing.assert_allclose(B_d_msd, B_d_rlc, atol=TOL_EXACT_DISC)

    def test_euler_discretization_preserves_isomorphism(self, linear_systems):
        """Euler on identical A,B should give identical discrete matrices."""
        msd, rlc = linear_systems
        dt = 0.01
        A_d_msd, B_d_msd = euler_discretize(msd.A, msd.B, dt)
        A_d_rlc, B_d_rlc = euler_discretize(rlc.A, rlc.B, dt)
        np.testing.assert_allclose(A_d_msd, A_d_rlc)
        np.testing.assert_allclose(B_d_msd, B_d_rlc)

    def test_discrete_trajectories_identical(self, linear_systems):
        """Discrete simulation of isomorphic systems should produce identical outputs."""
        msd, rlc = linear_systems
        dt = 0.01
        n_steps = 1000
        A_d, B_d = exact_discretize(msd.A, msd.B, dt)
        u_seq = np.ones((n_steps, 1))

        x_msd, y_msd = simulate_discrete(A_d, B_d, msd.C, msd.D, X0, u_seq)
        x_rlc, y_rlc = simulate_discrete(A_d, B_d, rlc.C, rlc.D, X0, u_seq)
        np.testing.assert_allclose(y_msd, y_rlc, atol=TOL_EXACT_DISC)

    def test_euler_error_grows_with_dt(self, linear_systems):
        """Euler discretization error should increase with larger dt."""
        msd, _ = linear_systems
        errors = []
        for dt in [0.001, 0.01, 0.1]:
            A_d_euler, B_d_euler = euler_discretize(msd.A, msd.B, dt)
            A_d_exact, B_d_exact = exact_discretize(msd.A, msd.B, dt)
            err = np.max(np.abs(A_d_euler - A_d_exact))
            errors.append(err)
        # Errors should be monotonically increasing
        assert errors[0] < errors[1] < errors[2]

    def test_rk4_more_accurate_than_euler(self, linear_systems):
        """RK4 discretization should be more accurate than Euler at same dt."""
        msd, _ = linear_systems
        dt = 0.1
        A_d_exact, _ = exact_discretize(msd.A, msd.B, dt)
        A_d_euler, _ = euler_discretize(msd.A, msd.B, dt)
        A_d_rk4, _ = rk4_discretize(msd.A, msd.B, dt)
        err_euler = np.max(np.abs(A_d_euler - A_d_exact))
        err_rk4 = np.max(np.abs(A_d_rk4 - A_d_exact))
        assert err_rk4 < err_euler
