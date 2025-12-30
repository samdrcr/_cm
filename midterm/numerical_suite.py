#范權榮 111210557
import numpy as np
import time

class NumerixSuite:
    def __init__(self):
        self.history = []

    def solve_newton_raphson(self, func, dfunc, x0, tol=1e-7, max_iter=100):
        """Finds roots of non-linear equations using the derivative."""
        print(f"\n[Running Newton-Raphson] Initial Guess: {x0}")
        x = x0
        start_time = time.time()
        
        for i in range(1, max_iter + 1):
            f_x = func(x)
            df_x = dfunc(x)
            
            if abs(df_x) < 1e-12:
                return None, "Derivative too small (Division by zero risk)."
                
            x_new = x - f_x / df_x
            error = abs(x_new - x)
            
            if error < tol:
                runtime = (time.time() - start_time) * 1000
                return x_new, i, runtime
            
            x = x_new
        return x, max_iter, 0

    def solve_gauss_seidel(self, A, b, tol=1e-7, max_iter=100):
        """Solves Ax = b iteratively."""
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)
        n = len(b)
        x = np.zeros(n)
        start_time = time.time()

        # Check for diagonal dominance for convergence stability
        diag = np.diag(np.abs(A))
        off_diag = np.sum(np.abs(A), axis=1) - diag
        if not np.all(diag > off_diag):
            print("Warning: Matrix is not diagonally dominant. Convergence not guaranteed.")

        for k in range(1, max_iter + 1):
            x_old = x.copy()
            for i in range(n):
                sum_j = sum(A[i][j] * x[j] for j in range(n) if i != j)
                x[i] = (b[i] - sum_j) / A[i][i]
            
            error = np.linalg.norm(x - x_old, ord=np.inf)
            if error < tol:
                runtime = (time.time() - start_time) * 1000
                return x, k, runtime
        return x, max_iter, 0

def main():
    suite = NumerixSuite()
    
    while True:
        print("\n" + "="*40)
        print("  NUMERIX: COMPUTATIONAL METHODS SUITE  ")
        print("="*40)
        print("1. Root Finding (Newton-Raphson)")
        print("2. Linear System (Gauss-Seidel)")
        print("3. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            # Example: f(x) = x^2 - 2
            f = lambda x: x**2 - 2
            df = lambda x: 2*x
            root, iters, dt = suite.solve_newton_raphson(f, df, x0=1.5)
            print(f"Root Found: {root:.6f}\nIterations: {iters}\nTime: {dt:.4f}ms")
            
        elif choice == '2':
            # Example system: 4x + y = 5, x + 3y = 4
            A = [[4, 1], [1, 3]]
            b = [5, 4]
            x, iters, dt = suite.solve_gauss_seidel(A, b)
            print(f"Solution: {x}\nIterations: {iters}\nTime: {dt:.4f}ms")
            
        elif choice == '3':
            break

if __name__ == "__main__":
    main()

#范權榮 111210557