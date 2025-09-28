#范權榮 111210557
import numpy as np

def find_roots(coeff_list):
    while len(coeff_list) > 1 and abs(coeff_list[-1]) < 1e-14:
        coeff_list.pop()

    degree = len(coeff_list) - 1

    if degree == 0:
        return "no roots"
    if degree == 1:
        return [-coeff_list[0] / coeff_list[1]]

    mat = np.zeros((degree, degree))
    mat[1:, :-1] = np.eye(degree - 1)
    mat[0, :] = -np.array(coeff_list[:-1])

    result = np.linalg.eigvals(mat)
    return result

poly = [-8, 14, -7, 1]
print(find_roots(poly))
