import numpy as np


def braunschweig(compos: np.matrix) -> float:
    K = compos[0, 0]
    Na = compos[0, 1]
    N = compos[0, 2]
    return (0.12 * (K + Na) + 0.24 * N + 0.48) / 100


def get_inorganic(prod_val: np.matrix, compos_inorganic: np.matrix) -> np.matrix:
    num_days, num_varieties = prod_val.shape
    new_prod_val = np.matrix(prod_val)

    for variety in range(num_varieties):
        braun_res = braunschweig(compos_inorganic[variety])
        for day in range(num_days):
            if braun_res < new_prod_val[day, variety]:
                new_prod_val[day, variety] -= braun_res
            else:
                new_prod_val[day, variety] = 0

    return new_prod_val








