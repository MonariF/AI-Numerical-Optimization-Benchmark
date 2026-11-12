import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from reference_solution import objective, solve_problem


def test_objective_at_known_solution():
    assert abs(objective([0.0, 2.0]) - 3.0) < 1e-12


def test_solver_reports_success():
    assert solve_problem()["result"].success


def test_solution_matches_analytical_optimum():
    solution = solve_problem()
    assert abs(solution["x"]) < 1e-5
    assert abs(solution["y"] - 2.0) < 1e-5
    assert abs(solution["objective"] - 3.0) < 1e-6


def test_solution_is_feasible():
    solution = solve_problem()
    assert solution["constraint_residual"] >= -1e-7
    assert solution["x"] >= -1e-7
    assert solution["y"] >= -1e-7
