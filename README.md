# Hybrid Quantum vs Classical Optimization

## Overview
This repository contains an implementation of a hybrid quantum-classical and a purely classical approach to solving an optimization problem. The quantum approach leverages D-Wave's Leap Hybrid Constrained Quadratic Model (CQM) Sampler, while the classical approach utilizes IBM Qiskit's `CplexOptimizer` for solving Quadratic Programming problems. A performance comparison is provided.

## Repository Contents
- **`Hybrid_quantum.py`**: Main script that formulates and solves the problem using a hybrid quantum-classical approach.
- **`classicalSolver.py`**: Implements a purely classical approach using IBM Qiskit's `CplexOptimizer`.
- **`Quantum-Cplex.png`**: Visualization comparing the performance of the quantum-classical hybrid solver versus the classical solver.

## Problem Formulation
The optimization problem is formulated as a Constrained Quadratic Model (CQM):
1. **Objective Function**: Defined using random variables `mu` and `sigma` to model an arbitrary optimization problem.
2. **Constraint**: The solution must satisfy the constraint that the sum of selected variables equals a predefined value (e.g., `4`).

## Implementation Details
### 1. Hybrid Quantum Approach
- **File**: `Hybrid_quantum.py`
- Constructs the problem using `dimod` and formulates a quadratic objective function.
- Uses the `LeapHybridCQMSampler()` from D-Wave to solve the optimization problem.
- Extracts feasible solutions and determines the best one.
- Execution time is measured using `timeit`.

### 2. Classical Solver Approach
- **File**: `classicalSolver.py`
- Constructs the problem using `docplex` and formulates a Quadratic Program using Qiskit's `QuadraticProgram`.
- Uses the `CplexOptimizer()` from Qiskit to solve the problem.
- Execution time is measured and printed.

### 3. Performance Comparison
- The provided visualization (`Quantum-Cplex.png`) compares the runtime of the quantum-classical hybrid solver with the purely classical solver.
- The plot demonstrates that the classical solver struggles to converge with large problem sizes, while the hybrid quantum solver maintains stable performance.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.x
- `dimod` (D-Wave's Discrete Modeling package)
- `dwave-system` (for interacting with D-Wave quantum computers)
- `numpy` (for numerical computations)
- `qiskit-optimization` (for classical optimization)
- `docplex` (for mathematical modeling)

You can install dependencies using:
```sh
pip install dimod dwave-system numpy qiskit-optimization docplex
```

## Running the Code
### Hybrid Quantum Solver
Execute the script using:
```sh
python Hybrid_quantum.py
```

### Classical Solver
Execute the script using:
```sh
python classicalSolver.py
```

## Results
- The scripts print the formulated problem, the solution from each solver, and execution time.
- The output image (`Quantum-Cplex.png`) provides a visual representation of solver performance.

## Future Work
- Extend the problem formulation to real-world datasets.
- Experiment with different constraints and objective functions.
- Compare results with other classical solvers such as Gurobi or SCIP.

