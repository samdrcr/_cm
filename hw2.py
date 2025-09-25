import cmath

p = 1
q = -2
r = 3

def find_roots(x, y, z):
    delta = y ** 2 - 4 * x * z

    if delta != 0:
        sol1 = (-y + cmath.sqrt(delta)) / (2 * x)
        sol2 = (-y - cmath.sqrt(delta)) / (2 * x)
    else:
        sol1 = -y / (2 * x)
        sol2 = sol1
    return sol1, sol2

ans1, ans2 = find_roots(p, q, r)
print("Root 1 =", ans1)
print("Root 2 =", ans2)
