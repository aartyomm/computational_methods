import numpy as np
from scipy.optimize import linear_sum_assignment


class Algorithm:

    def __init__(self, name: str, func, num_days: int):
        self.name = name
        self.func = func
        self.ans: list[float] = [0.0] * num_days

    def __call__(self, matrix: np.matrix):
        return self.func(matrix)


class Algorithms:
    def __init__(self, num_days: int):
        self.__algorithms = [
            Algorithm('Венгерский мин', self.__hungarian_min, num_days),
            Algorithm('Венгерский макс', self.__hungarian_max, num_days),
            Algorithm('Жадный', self.__greedy_max, num_days),
            Algorithm('Бережливый', self.__greedy_min, num_days),
            Algorithm('Жадно-бережливый', self.__greedy_thrifty, num_days),
            Algorithm('Бережливо-жадный', self.__thrifty_greedy, num_days)
        ]
        self.num_days = num_days

    def __getitem__(self, item):
        return self.__algorithms[item]

    def __len__(self):
        return len(self.__algorithms)

    def run_algorithms(self, matrix: np.matrix):
        for algorithm in self.__algorithms:
            row_ind, col_ind = algorithm(matrix)
            for i in range(self.num_days):
                algorithm.ans[i] += matrix[row_ind[i], col_ind[i]]

    def calculate_average(self, t: int):
        for algorithm in self.__algorithms:
            algorithm.ans[0] /= t
            for i in range(1, self.num_days):
                algorithm.ans[i] /= t
                algorithm.ans[i] += algorithm.ans[i - 1]

    @staticmethod
    def __hungarian_max(P: np.matrix):
        return linear_sum_assignment(P, True)

    @staticmethod
    def __hungarian_min(P: np.matrix):
        return linear_sum_assignment(P, False)

    @staticmethod
    def __greedy_max(P: np.matrix):
        return Algorithms.__greedy(P, True)

    @staticmethod
    def __greedy_min(P: np.matrix):
        return Algorithms.__greedy(P, False)

    @staticmethod
    def __greedy(P: np.matrix, is_max: bool) -> tuple[list[int], list[int]]:
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

    @staticmethod
    def __greedy_thrifty(P: np.matrix) -> tuple[list[int], list[int]]:
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

    @staticmethod
    def __thrifty_greedy(P: np.matrix) -> tuple[list[int], list[int]]:
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