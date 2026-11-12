# Evaluator Notes — Deliberately Flawed Candidate

Expected errors in `src/flawed_candidate.py`:

1. **Objective sign reversed:** minimizing the negative of the requested objective maximizes the requested objective.
2. **Inequality sign reversed:** SLSQP expects inequality functions to be non-negative. Correct function: `2 - x - y`, not `x + y - 2`.
3. **Bounds omitted:** the task requires `x >= 0` and `y >= 0`.
4. **No convergence check:** code prints the result without checking `result.success` or the solver message.
5. **Unsupported conclusion:** it does not independently check feasibility; the claim that constraints are inactive is false at the true solution.

## Evaluator exercise
Ask an AI system to review the flawed candidate against `task/benchmark_task.md`. Score the review with `rubric.md`. A strong review diagnoses each error, explains its consequence, and provides corrected code with independent feasibility checks.

Do not treat fluent explanation or code execution alone as proof of correctness.
