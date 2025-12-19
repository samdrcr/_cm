import numpy as np
import re

def solve_ode_general(coefficients):
    roots = np.roots(coefficients)
    solution_parts = []
    C_index = 1
    used = set()

    for r in roots:
        key = tuple(np.round([r.real, r.imag], 10))
        if key in used:
            continue

        multiplicity = sum(1 for rr in roots if np.isclose(r, rr))
        used.add(key)
        a, b = r.real, r.imag

        if np.isclose(b, 0):
            for m in range(multiplicity):
                power = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                term = f"C_{C_index}{power}e^({a:.1f}x)"
                solution_parts.append(term)
                C_index += 1
        else:
            for m in range(multiplicity):
                power = f"x^{m} " if m > 1 else ("x " if m == 1 else "")
                term1 = f"C_{C_index} {power}e^({a:.1f}x) cos({abs(b):.1f}x)"
                solution_parts.append(term1)
                C_index += 1
                term2 = f"C_{C_index} {power}e^({a:.1f}x) sin({abs(b):.1f}x)"
                solution_parts.append(term2)
                C_index += 1

    return " + ".join(solution_parts)

class MathCompiler:
    def __init__(self):
        self.ode_pattern = r"solve_ode\s*\{\s*([^}]+)\s*\};"
        self.assign_pattern = r"(\w+)\s*=\s*(\d+);"

    def compile(self, code):
        print(".text")
        print(".global main")
        print("main:")

        lines = code.strip().split('\n')
        for line in lines:
            assign_match = re.search(self.assign_pattern, line)
            if assign_match:
                var, val = assign_match.groups()
                print(f"  li t0, {val}  # {var} = {val}")

            ode_match = re.search(self.ode_pattern, line)
            if ode_match:
                coeffs = [float(c.strip()) for c in ode_match.group(1).split(',')]
                result = solve_ode_general(coeffs)
                print(f"  # ODE Solution: {result}")

        print("  li a0, 0")
        print("  ret")

if __name__ == "__main__":
    test_code = """
    alpha = 5;
    solve_ode {1, -3, 2};
    solve_ode {1, 0, 4};
    """
    
    compiler = MathCompiler()
    compiler.compile(test_code)