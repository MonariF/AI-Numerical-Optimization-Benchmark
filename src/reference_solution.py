import numpy as np
from scipy.optimize import minimize


def objective(z):
    # Convex objective f(x,y) = (x-1)^2 + 2(y-3)^2
    x, y = np.asarray(z, dtype=float)
    return float((x - 1.0) ** 2 + 2.0 * (y - 3.0) ** 2)


def solve_problem():
    # SLSQP inequality convention: constraint function must be >= 0.
    constraints = [{"type": "ineq", "fun": lambda z: 2.0 - z[0] - z[1]}]
    bounds = [(0.0, None), (0.0, None)]
    result = minimize(
        objective,
        x0=np.array([0.5, 0.5]),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
        options={"ftol": 1e-12, "maxiter": 500, "disp": False},
    )
    if not result.success:
        raise RuntimeError(f"Optimization did not converge: {result.message}")

    x, y = result.x
    residual = 2.0 - x - y
    tol = 1e-7
    if residual < -tol or x < -tol or y < -tol:
        raise RuntimeError("Solver returned an infeasible point.")

    return {
        "result": result,
        "x": float(x),
        "y": float(y),
        "objective": float(result.fun),
        "constraint_residual": float(residual),
    }


def main():
    solution = solve_problem()
    result = solution["result"]
    print("Constrained optimization benchmark")
    print("Method: SLSQP")
    print(f"Success: {result.success}")
    print(f"Message: {result.message}")
    print(f"Iterations: {result.nit}")
    print(f"x*: {solution['x']:.10f}")
    print(f"y*: {solution['y']:.10f}")
    print(f"Minimum objective: {solution['objective']:.10f}")
    print(f"Constraint residual (2 - x - y): {solution['constraint_residual']:.3e}")
    print("Analytical optimum: (0, 2), objective = 3.")


if __name__ == "__main__":
    main()
