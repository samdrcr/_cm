# MidTerm Project: Numerical Methods Implementation
**范權榮 111210557*
**Course:** Coding and Math
**Topic:** Iterative Solvers and Root Finding

## Project Overview
This repository contains my implementation of key numerical algorithms for the Midterm assignment. The goal of this project was to move beyond simple manual calculations and develop a reusable Python-based suite that can solve complex systems of equations efficiently.

While many of my peers focused on individual scripts, I decided to build a "Suite" structure to handle different mathematical problems under a single execution flow.

## Implemented Methods

### 1. Newton-Raphson Method (Root Finding)
I chose this method because of its quadratic convergence rate. It is significantly faster than the Bisection method, provided the initial guess is reasonable.
* **Logic:** It uses the tangent line of the function $f(x)$ to approximate the root.
* **Formula:** $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
* **Safety Feature:** I added a check to prevent division by zero if the derivative becomes too small ($< 10^{-12}$).

### 2. Gauss-Seidel Method (Linear Systems)
For solving $Ax = b$, the Gauss-Seidel method was implemented. It is an improvement over the Jacobi method because it uses the most recently updated values immediately within the same iteration.
* **Optimization:** The code includes a check for **Diagonal Dominance**. I realized during testing that if the matrix isn't diagonally dominant, the code might diverge, so I added a warning log for the user.
* **Stopping Criterion:** The iteration stops when the Infinity Norm of the error falls below the tolerance level (default $10^{-7}$).

## Development & Credits
During the development of this project, I ran into several issues regarding matrix convergence and Python's handling of floating-point precision. 

To refine my logic and ensure my algorithms were optimized for performance, I consulted with **Gemini (AI Thought Partner)**. The AI helped me:
* Structure the code into a Python `class` for better organization.
* Implement the `time` tracking logic to measure algorithm efficiency.
* Draft this documentation to clearly communicate the mathematical concepts used.

While the core logic and implementation were driven by my course requirements, the AI assistance allowed me to add "quality of life" features like the runtime measurement and the convergence warnings.

## How to Run
1. Ensure you have `numpy` installed: `pip install numpy`
2. Run the main script: `python main.py`
3. Follow the CLI prompts to test the predefined mathematical models.

---
*Created as part of the _cm Midterm Assignment.*