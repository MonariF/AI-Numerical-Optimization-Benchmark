# AI Evaluation Benchmark: Numerical Optimization and Scientific Computing

**Author:** Dr. Fred Nyamitago Monari, PhD  
**Specialization:** Applied Statistics | Computational Mathematics | Numerical Optimization

---

## 1. Project Overview

This project demonstrates the formulation, implementation, verification and evaluation of numerical optimization problems using Python and SciPy.

The benchmark evaluates the ability to correctly formulate mathematical optimization problems, implement objective functions and constraints, select numerical algorithms, verify convergence and assess the mathematical validity of computational solutions.

It includes:

- Mathematical optimization problem specifications.
- Reproducible Python reference implementations.
- Intentionally flawed candidate solutions.
- Analytical verification using optimization theory.
- Objective evaluation rubrics.
- Automated tests for numerical accuracy and feasibility.

**Transparency Statement:** This is an independently developed academic portfolio project. It demonstrates relevant computational and AI-evaluation skills but does not represent previous paid AI-training or commercial AI-model evaluation employment.

## 2. Mathematical Optimization Problem

The benchmark considers the following constrained convex optimization problem.

**Objective function**

Minimize:

\[
f(x,y)=(x-1)^2+2(y-3)^2
\]

Subject to:

\[
x+y\leq 2
\]

\[
x\geq 0,\qquad y\geq 0
\]

**Analytical solution**

The unique optimal solution is:

\[
x^*=0,\qquad y^*=2
\]

The minimum objective value is:

\[
f(x^*,y^*)=3
\]

Both the non-negativity constraint on \(x\) and the linear inequality constraint are active at the optimum.

## 3. Technical Competencies

**Computational Mathematics**
- Mathematical formulation of constrained optimization problems.
- Convex optimization and feasible regions.
- Numerical optimization algorithms.
- Karush-Kuhn-Tucker (KKT) conditions.
- Gradient-based optimization.
- Numerical convergence and stability.

**Scientific Computing**
- Python-based numerical computation.
- SciPy optimization algorithms.
- Objective function implementation.
- Constraint and bound specification.
- Numerical feasibility verification.
- Reproducible computational experiments.

**AI Model Evaluation**
- Evaluation of AI-generated mathematical solutions.
- Identification of incorrect optimization formulations.
- Detection of numerical and logical errors.
- Validation of solver outputs.
- Development of objective scoring rubrics.
- Verification of mathematical reasoning against analytical solutions.

## 4. Repository Structure

```text
AI-Numerical-Optimization-Benchmark/
│
├── README.md
├── requirements.txt
│
├── task/
│   └── benchmark_task.md
│
├── src/
│   ├── reference_solution.py
│   └── flawed_candidate.py
│
├── evaluation/
│   ├── rubric.md
│   └── evaluator_notes.md
│
└── tests/
    └── test_reference_solution.py
```

## 5. Installation and Reproducibility

**Requirements:** Python 3.10 or later.

### Step 1: Clone the repository

```bash
git clone https://github.com/MonariF/AI-Numerical-Optimization-Benchmark.git

cd AI-Numerical-Optimization-Benchmark
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the reference implementation

```bash
python src/reference_solution.py
```

### Step 5: Execute automated tests

```bash
python -m pytest -q
```

## 6. Expected Computational Results

The reference implementation uses the Sequential Least Squares Programming (SLSQP) algorithm from `scipy.optimize.minimize`.

| Parameter | Expected result |
|---|---:|
| Optimal x | 0 |
| Optimal y | 2 |
| Minimum objective | 3 |
| Solver | SLSQP |
| Convergence status | Successful |
| Constraint residual | Approximately 0 |

Numerical solvers operate using floating-point arithmetic and tolerances. Small numerical deviations from the analytical solution are expected.

## 7. Analytical Verification: KKT Conditions

The problem can be expressed using the inequality constraints:

\[
g_1(x,y)=x+y-2\leq0
\]

\[
g_2(x,y)=-x\leq0
\]

\[
g_3(x,y)=-y\leq0
\]

At the optimal point \((0,2)\), the corresponding KKT multipliers are:

\[
\lambda_1=4,\quad \lambda_2=2,\quad \lambda_3=0
\]

These multipliers satisfy:

- Primal feasibility.
- Dual feasibility.
- Stationarity.
- Complementary slackness.

Since the objective is strictly convex and the feasible region is convex, the KKT conditions establish the unique global optimum.

## 8. AI Evaluation Framework

The benchmark includes a 100-point scoring rubric for assessing AI-generated optimization solutions.

| Evaluation criterion | Weight |
|---|---:|
| Mathematical formulation | 15 |
| Objective function implementation | 10 |
| Constraint and bounds implementation | 20 |
| Solver selection and execution | 10 |
| Convergence diagnostics | 10 |
| Feasibility verification | 10 |
| Numerical accuracy | 10 |
| Analytical and KKT reasoning | 10 |
| Technical communication | 5 |
| **Total** | **100** |

Critical errors, such as reversing inequality constraints, omitting required bounds, maximizing instead of minimizing, or reporting infeasible solutions as valid, attract substantial penalties.

A successful solver status alone is not sufficient evidence of mathematical correctness. Independent verification is required.

## 9. Technical Tools

- Python
- NumPy
- SciPy
- pytest

## 10. Research and Professional Background

Dr. Fred Nyamitago Monari is a Computational Mathematician and Applied Statistician holding a PhD in Applied Statistics.

He is a Lecturer and Research Fellow at Kisii University, Kenya, with professional experience in mathematical modelling, computational statistics, quantitative research and data science.

His research interests include numerical methods, optimization, machine learning, statistical modelling, AI-enabled scientific research and computational data analysis.

He has authored and co-authored more than 20 research publications.

## 11. Limitations and Future Development

This is a compact educational benchmark designed around a well-defined convex optimization problem. It does not comprehensively assess all classes of optimization problems or large-scale computational performance.

Future extensions include:

- Rosenbrock function and nonlinear optimization.
- Linear programming using SciPy.
- Mixed-integer optimization using OR-Tools or Pyomo.
- Sensitivity and numerical conditioning analysis.
- Gradient and Hessian verification.
- Advanced convergence and stability testing.

---

**GitHub Repository:** https://github.com/MonariF/AI-Numerical-Optimization-Benchmark

**Contact:** fnyamitago@gmail.com
