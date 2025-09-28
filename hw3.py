#范權榮 111210557
import cmath

def solve_cubic(p, q, r, s):
    m, n, o = q/p, r/p, s/p

    u = n - (m*m)/3
    v = (2*m*m*m)/27 - (m*n)/3 + o

    delta = (v/2)**2 + (u/3)**3

    root_part = cmath.sqrt(delta)
    alpha = (-v/2 + root_part) ** (1/3)
    beta = (-v/2 - root_part) ** (1/3)

    omega = [
        1,
        -0.5 + cmath.sqrt(3)/2*1j,
        -0.5 - cmath.sqrt(3)/2*1j
    ]

    roots = []
    for i in range(3):
        temp = alpha * omega[i] + beta * omega[(3 - i) % 3]
        final = temp - m/3
        roots.append(final)

    return roots

print(solve_cubic(1, -6, 11, -6))
