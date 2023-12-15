import numpy as np
from scipy.optimize import linear_sum_assignment


class Algorithm:

    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.ans: list[float] | None = None

    def __call__(self, matrix: np.matrix):
        return self.func(matrix)


def hungarian_max(P: np.matrix):
    return linear_sum_assignment(P, True)


def hungarian_min(P: np.matrix):
    return linear_sum_assignment(P, False)


def greedy_max(P: np.matrix):
    return greedy(P, True)


def greedy_min(P: np.matrix):
    return greedy(P, False)


def greedy(P: np.matrix, is_max: bool) -> tuple[list[int], list[int]]:
    n, m = P.shape
    used = [False] * m
    row_ind = [i for i in range(n)]
    col_ind = [0] * n

    for i in range(n):
        cur_ind = -1
        cur_val = -1.0 if is_max else float('inf')

        for j in range(m):
            if not used[j]:
                if is_max:
                    if P[i, j] > cur_val:
                        cur_val = P[i, j]
                        cur_ind = j
                else:
                    if P[i, j] < cur_val:
                        cur_val = P[i, j]
                        cur_ind = j
        col_ind[i] = cur_ind
        used[cur_ind] = True

    return row_ind, col_ind


def greedy_thrifty(P: np.matrix) -> tuple[list[int], list[int]]:
    n, m = P.shape
    theta = int(m/2)
    used = [False] * m
    row_ind = [i for i in range(n)]
    col_ind = [0] * n
    for i in range(theta):
        cur_ind = -1
        cur_val = -1.0
        for j in range(m):
            if not used[j]:
                if P[i, j] > cur_val:
                    cur_val = P[i, j]
                    cur_ind = j
        col_ind[i] = cur_ind
        used[cur_ind] = True
    for i in range(theta, n):
        cur_ind = -1
        cur_val = float('inf')

        for j in range(m):
            if not used[j]:
                if P[i, j] < cur_val:
                    cur_val = P[i, j]
                    cur_ind = j
        col_ind[i] = cur_ind
        used[cur_ind] = True
        
    return row_ind, col_ind


def thrifty_greedy(P: np.matrix) -> tuple[list[int], list[int]]:
    n, m = P.shape
    theta = int(m/2)
    used = [False] * m
    row_ind = [i for i in range(n)]
    col_ind = [0] * n
    for i in range(theta):
        cur_ind = -1
        cur_val = float('inf')

        for j in range(m):
            if not used[j]:
                if P[i, j] < cur_val:
                    cur_val = P[i, j]
                    cur_ind = j
        col_ind[i] = cur_ind
        used[cur_ind] = True
    for i in range(theta, n):
        cur_ind = -1
        cur_val = -1.0

        for j in range(m):
            if not used[j]:
                if P[i, j] > cur_val:
                    cur_val = P[i, j]
                    cur_ind = j
        col_ind[i] = cur_ind
        used[cur_ind] = True
        
    return row_ind, col_ind