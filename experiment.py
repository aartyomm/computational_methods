from random import uniform
import numpy as np
from algorithms import Algorithm
from graph import show_graph


def generate_matrix(n: int, min_a: float, max_a: float, min_b: float, max_b: float) -> np.matrix:
    matrix = [[0.0] * n for _ in range(n)]
    number_digits = 3  # Количество чисел после запятой

    for i in range(n):
        matrix[0][i] = round(uniform(min_a, max_a), number_digits)
        for j in range(1, n):
            matrix[j][i] = round(matrix[j - 1][i] * uniform(min_b, max_b), number_digits)

    return np.matrix(np.array(matrix))


def experiment(n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float, algorithms: list[Algorithm]):
    for algorithm in algorithms:
        algorithm.ans = [0.0] * n

    for _ in range(t):
        P = generate_matrix(n, min_a, max_a, min_b, max_b)
        for algorithm in algorithms:
            row_ind, col_ind = algorithm(P)
            for i in range(n):
                algorithm.ans[i] += P[row_ind[i], col_ind[i]]

    for algorithm in algorithms:
        algorithm.ans[0] /= n
        for i in range(1, n):
            algorithm.ans[i] /= n
            algorithm.ans[i] += algorithm.ans[i - 1]

    show_graph(algorithms)
