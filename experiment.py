from random import uniform
from numpy.random import normal
import numpy as np
from algorithms import Algorithm
from graph import show_graph
from inorganic_influence import get_inorganic


def generate_uniform_matrix(n: int, min_a: float, max_a: float, min_b: float, max_b: float) -> np.matrix:
    matrix = [[0.0] * n for _ in range(n)]
    number_digits = 3  # Количество чисел после запятой

    for i in range(n):
        matrix[0][i] = round(uniform(min_a, max_a), number_digits)
        for j in range(1, n):
            matrix[j][i] = round(matrix[j - 1][i] * uniform(min_b, max_b), number_digits)

    return np.matrix(np.array(matrix))


def generate_normal_matrix(n: int, min_a: float, max_a: float, avg: float, deviation: float) -> np.matrix:
    matrix = [[0.0] * n for _ in range(n)]
    number_digits = 3  # Количество чисел после запятой

    for i in range(n):
        matrix[0][i] = round(uniform(min_a, max_a), number_digits)
        normal_row = normal(avg, deviation, n)
        normal_row = np.clip(normal_row, 0.001, 0.999)
        for j in range(1, n):
            matrix[j][i] = round(matrix[j-1][i] * float(normal_row[j]), number_digits)

    return np.matrix(np.array(matrix))


def generate_inorganic_matrix(n: int) -> np.matrix:
    min_K = 4
    max_K = 8.7
    min_Na = 0.15
    max_Na = 0.92
    min_N = 1.2
    max_N = 3
    number_digits = 3  # Количество чисел после запятой

    matrix = [[0.0] * 3 for _ in range(n)]

    for i in range(n):
        matrix[i][0] = round(uniform(min_K, max_K), number_digits)
        matrix[i][1] = round(uniform(min_Na, max_Na), number_digits)
        matrix[i][2] = round(uniform(min_N, max_N), number_digits)

    return np.matrix(np.array(matrix))


def reset_ans(algorithms: list[Algorithm], n: int) -> None:
    for algorithm in algorithms:
        algorithm.ans = [0.0] * n


def run_algorithms(algorithms: list[Algorithm], matrix: np.matrix, n: int) -> None:
    for algorithm in algorithms:
        row_ind, col_ind = algorithm(matrix)
        for i in range(n):
            algorithm.ans[i] += matrix[row_ind[i], col_ind[i]]


def experiment(n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float, algorithms: list[Algorithm],
               consider_inorganic: bool, is_normal: bool):
    reset_ans(algorithms, n)

    for _ in range(t):
        if is_normal:
            P = generate_normal_matrix(n, min_a, max_a, min_b, max_b)
        else:
            P = generate_uniform_matrix(n, min_a, max_a, min_b, max_b)

        if consider_inorganic:
            inorganic_matrix = generate_inorganic_matrix(n)
            P = get_inorganic(P, inorganic_matrix)

        run_algorithms(algorithms, P, n)

    for algorithm in algorithms:
        algorithm.ans[0] /= t
        for i in range(1, n):
            algorithm.ans[i] /= t
            algorithm.ans[i] += algorithm.ans[i - 1]

    return algorithms
