from random import uniform
from numpy.random import normal
import numpy as np
from algorithms import Algorithms
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


def experiment(n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float,
               consider_inorganic: bool, is_normal: bool) -> Algorithms:

    algorithms = Algorithms(n)
    for _ in range(t):
        if is_normal:
            P = generate_normal_matrix(n, min_a, max_a, min_b, max_b)
        else:
            P = generate_uniform_matrix(n, min_a, max_a, min_b, max_b)

        if consider_inorganic:
            inorganic_matrix = generate_inorganic_matrix(n)
            P = get_inorganic(P, inorganic_matrix)

        algorithms.run_algorithms(P)

    algorithms.calculate_average(t)
    return algorithms
