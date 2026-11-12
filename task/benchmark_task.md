# Benchmark Task 002: Constrained Numerical Optimization with SciPy

## Problem
Minimize `f(x,y) = (x - 1)^2 + 2(y - 3)^2` subject to:
- `x + y <= 2`
- `x >= 0`
- `y >= 0`

## Candidate instructions
Use Python and SciPy to:
1. Implement the objective function correctly.
2. Translate the inequality into the convention expected by the solver. For SLSQP, an inequality function must be non-negative at feasible points.
3. Apply the non-negativity bounds.
4. Solve using `scipy.optimize.minimize` and an appropriate method such as SLSQP.
5. Report the optimizer, decision variables, objective value, success flag, iteration information and constraint residual.
6. Independently verify feasibility.
7. Explain why the numerical solution agrees with the analytical optimum.
8. Provide executable, reproducible code.

## Analytical check
The unique solution is `(x*, y*) = (0, 2)`, with `f(x*,y*)=3`.

For `g1=x+y-2<=0`, `g2=-x<=0`, and `g3=-y<=0`, KKT multipliers at `(0,2)` are `lambda1=4`, `lambda2=2`, and `lambda3=0`. They are non-negative; stationarity, primal feasibility and complementary slackness hold.

## Required output
Executable code; optimal x and y; minimum objective; solver status and message; feasibility residuals; short numerical and analytical verification.

## Critical errors
Reversing the inequality sign; omitting non-negativity bounds; maximizing rather than minimizing; failing to check `result.success`; treating solver success as proof of feasibility or global optimality; claiming constraints are inactive when they bind.
