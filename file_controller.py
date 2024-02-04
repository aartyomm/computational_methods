import csv
from typing import Any
from algorithms import Algorithms
import os
import shutil


class FileController:
    tmp_path_for_experiment: str | None = None
    tmp_path_for_matrix: str | None = None

    @staticmethod
    def save_experiment_result(path: str, n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float,
                               consider_inorganic: bool, is_normal: bool, algorithms: Algorithms, errors: tuple):

        parameters = [['n', n, ''], ['t', t, ''], ['a', f'[{min_a}; {max_a}]', ''],
                      ['Распределение b', 'Нормальное' if is_normal else 'Равномерное', '']]
        answer = FileController.__generate_answer(algorithms, errors)
        if is_normal:
            parameters.append(['b', f'a={min_b}; b={max_b}', ''])
        else:
            parameters.append(['b', f'[{min_b}; {max_b}]', ''])
        parameters.append(['Влияние неорганики', 'Да' if consider_inorganic else 'Нет', ''])

        with open(path, mode='w') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerow(['Параметры', 'Значение', '', 'Алгоритм', 'Результат', '',
                             'Относительная погрешность', 'Значение'])
            for i in range(len(answer)):
                writer.writerow(parameters[i] + answer[i])

    @staticmethod
    def __generate_answer(algorithms: Algorithms, errors: tuple) -> tuple[list[str | Any]]:
        answer = []
        error_names = ['Жадный к максимуму', 'Бережливый к минимуму', 'Жадно-бережливый к максимуму',
                       'Жадно-бережливый к минимуму', 'Бережливо-Жадный к максимуму', 'Бережливо-Жадный к минимуму']
        for i in range(len(algorithms)):
            cur = [algorithms[i].name, round(algorithms[i].ans[-1], 2), '', error_names[i], f'{errors[i]}%']
            answer.append(cur)
        return tuple(answer)

    @staticmethod
    def save_matrix_result(path: str, matrix: list[list[float]], algorithms: Algorithms, errors: tuple):
        with open(path, mode='w') as file:
            answer = FileController.__generate_answer(algorithms, errors)
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            row = [''] * (len(matrix) + 2) + [algorithm.name for algorithm in algorithms] + [
                '', 'Алгоритм', 'Результат', '', 'Относительная погрешность', 'Значение']
            writer.writerow(row)
            row = [''] * (len(matrix) + 1) + ['День'] + ['Выбранный сорт'] * len(algorithms) + [''] + answer[0]
            writer.writerow(row)
            for i in range(len(matrix)):
                row = matrix[i]
                row.extend(['', i + 1])
                row.extend([algorithm.column_indexes[i] + 1 for algorithm in algorithms])
                if i + 1 < len(answer):
                    row.extend([''] + answer[i + 1])
                writer.writerow(row)
            for i in range(i + 2, len(answer)):
                row = [''] * (len(matrix) + 3 + len(algorithms)) + answer[i]
                writer.writerow(row)

    @staticmethod
    def __make_tmp_dir() -> str:
        path_to_dir = os.getcwd() + '/tmp'
        if not os.path.exists(path_to_dir):
            os.mkdir(path_to_dir)
        return path_to_dir

    @staticmethod
    def tmp_save_experiment(n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float,
                            consider_inorganic: bool, is_normal: bool, algorithms: Algorithms, errors: tuple):
        path_to_dir = FileController.__make_tmp_dir()
        if FileController.tmp_path_for_experiment is None:
            FileController.tmp_path_for_experiment = path_to_dir + '/tmp_experiment.csv'

        FileController.save_experiment_result(FileController.tmp_path_for_experiment, n, t, min_a, max_a, min_b, max_b,
                                              consider_inorganic, is_normal, algorithms, errors)

    @staticmethod
    def tmp_save_matrix(matrix: list[list[float]], algorithms: Algorithms, errors: tuple):
        path_to_dir = FileController.__make_tmp_dir()
        if FileController.tmp_path_for_matrix is None:
            FileController.tmp_path_for_matrix = path_to_dir + '/tmp_matrix.csv'
        FileController.save_matrix_result(FileController.tmp_path_for_matrix, matrix, algorithms, errors)

    @staticmethod
    def user_save_experiment(user_path: str):
        return shutil.copy(FileController.tmp_path_for_experiment, user_path)

    @staticmethod
    def user_save_matrix(user_path: str):
        return shutil.copy(FileController.tmp_path_for_matrix, user_path)

    @staticmethod
    def read_experiment_params(path: str) -> tuple:
        with open(path) as file:
            n = int(file.readline())
            min_a, max_a = map(float, file.readline().split())
            is_normal = int(file.readline())
            min_b, max_b = map(float, file.readline().split())
            consider_inorganic = int(file.readline())
            t = int(file.readline())

        return n, min_a, max_a, is_normal, min_b, max_b, consider_inorganic, t

    @staticmethod
    def read_matrix(path: str) -> tuple[int, list[list[float]]]:
        with open(path) as file:
            n = int(file.readline())
            matrix = [[] for _ in range(n)]
            for i in range(n):
                matrix[i] = list(map(float, file.readline().split()))
        return n, matrix




