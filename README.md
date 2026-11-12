# AI Evaluation Benchmark: Numerical Optimization and Scientific Computing

**Author:** Dr. Fred Nyamitago Monari, PhD  
**Specialization:** Applied Statistics | Computational Mathematics | Numerical Optimization

## Project overview
This independent portfolio project demonstrates the formulation, implementation, verification and evaluation of numerical optimization problems using Python and SciPy.

The benchmark uses a constrained convex optimization problem with a known analytical solution. It tests mathematical formulation, correct coding of constraints, solver selection, convergence checks, feasibility and interpretation.

**Transparency statement:** This is a self-directed portfolio project. It demonstrates relevant computational and evaluation skills; it is not evidence of previous paid AI-training or commercial AI-model evaluation employment.

## Benchmark problem

Minimize

`f(x,y) = (x - 1)^2 + 2(y - 3)^2`

subject to `x + y <= 2`, `x >= 0`, and `y >= 0`.

The unique optimum is `(x*, y*) = (0, 2)`, with objective value `3`. Both `x=0` and `x+y=2` are active at the optimum.

## Technical competencies
- Mathematical formulation of constrained optimization.
- Convex objective functions and feasible regions.
- Numerical optimization with `scipy.optimize.minimize`.
- Bounds and inequality constraints.
- Convergence and feasibility checks.
- Karush-Kuhn-Tucker (KKT) verification.
- Reproducible computational experiments.
- Evaluation of incorrect optimization code and reasoning.

## Repository structure
```text
AI-Numerical-Optimization-Benchmark/
├── README.md
├── requirements.txt
├── task/benchmark_task.md
├── src/reference_solution.py
├── src/flawed_candidate.py
├── evaluation/rubric.md
├── evaluation/evaluator_notes.md
└── tests/test_reference_solution.py
```

## Installation

Requires Python 3.10 or later.

```bash
python -m venv .venv
```

Windows activation:
```bash
.venv\Scripts\activate
```

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

Run reference solution:
```bash
python src/reference_solution.py
```

Run automated tests:
```bash
python -m pytest -q
```

## Expected result
- Optimal decision variables: `x = 0`, `y = 2` (within numerical tolerance).
- Minimum objective value: `3`.
- Inequality residual: `2 - x - y >= 0`.
- Bounds: `x >= 0`, `y >= 0`.
- Solver reports successful convergence.

## Analytical KKT check
For `g1=x+y-2<=0`, `g2=-x<=0`, and `g3=-y<=0`, the multipliers at `(0,2)` are `lambda1=4`, `lambda2=2`, and `lambda3=0`. They are non-negative; stationarity, primal feasibility and complementary slackness hold.

## Evaluation focus
The 100-point rubric assesses formulation, objective and constraint implementation, solver selection, convergence diagnostics, feasibility, numerical accuracy, KKT reasoning and communication.

A solver success flag alone is not proof of feasibility or global optimality. The candidate must independently verify the returned point.

## Limitations and future extensions
This is a compact educational benchmark, not a comprehensive test of all optimization classes or large-scale performance. Future extensions include Rosenbrock optimization, linear programming, mixed-integer optimization, sensitivity analysis, conditioning, and gradient/Hessian verification.
