# INTENTIONALLY FLAWED CANDIDATE — evaluator practice only.
import numpy as np
from scipy.optimize import minimize

def objective(z):
    x, y = z
    return -((x - 1.0) ** 2 + 2.0 * (y - 3.0) ** 2)  # Error 1: wrong sign; maximizes original objective.

# Error 2: SLSQP expects inequality functions >= 0; this sign is reversed.
constraints = [{"type": "ineq", "fun": lambda z: z[0] + z[1] - 2.0}]

# Error 3: required non-negativity bounds are missing.
result = minimize(objective, x0=np.array([0.5, 0.5]), method="SLSQP",
                  constraints=constraints)

# Error 4: no convergence or feasibility checks.
print("Optimal solution:", result.x)
print("Minimum objective:", result.fun)

# Error 5: unsupported claim; no KKT or independent feasibility check.
print("The constraints are inactive and the global minimum is verified.")
