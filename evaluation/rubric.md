# Scoring Rubric — Benchmark Task 002

Total: 100 points.

| Criterion | Points | Full-credit standard |
|---|---:|---|
| Mathematical formulation | 15 | Correct objective, variables and all constraints. |
| Objective implementation | 10 | Implements the requested function without sign/scaling errors. |
| Constraints and bounds | 20 | Correct SLSQP inequality sign and non-negativity bounds. |
| Solver selection and execution | 10 | Suitable method and executable code. |
| Convergence diagnostics | 10 | Checks success, status/message and iteration information. |
| Feasibility verification | 10 | Independently checks inequality residual and variable bounds. |
| Numerical accuracy | 10 | Solution close to (0,2), objective close to 3. |
| Analytical/KKT reasoning | 10 | Correctly explains active constraints and KKT consistency. |
| Communication/reproducibility | 5 | Reports assumptions, tolerances and reproducible steps. |

## Critical errors
Substantial deductions for reversing the inequality convention, omitting required bounds, maximizing instead of minimizing, failing to check solver status, or claiming feasibility/global optimality without verification.

A response solving a different optimization problem cannot pass merely because its code executes.

## Score bands
90–100 Excellent; 75–89 Good; 60–74 Borderline; 40–59 Poor; 0–39 Unacceptable.
