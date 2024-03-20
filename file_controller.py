import csv
from typing import Any
from PyQt6 import QtGui
from algorithms import Algorithms
from paths import Paths
import shutil
import os
from interface import validators


class FileController:
    tmp_path_for_experiment: str | None = None
    tmp_path_for_matrix: str | None = None

    @staticmethod
    def save_experiment_result(path: str, n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float,
                               consider_inorganic: bool, is_normal: bool, algorithms: Algorithms, errors: tuple):

        parameters = [['n', n, ''], ['t', t, ''], ['a', f'[{min_a}; {max_a}]', ''],
                      ['Distribution b', 'Concentrated' if is_normal else 'Uniform', '']]
        answer = FileController.__generate_answer(algorithms, errors)
        parameters.append(['b', f'[{min_b}; {max_b}]', ''])
        parameters.append(['Inorganic effects', 'Yes' if consider_inorganic else 'No', ''])

        with open(path, mode='w') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerow(['Parameters', 'Value', '', 'Algorithm', 'Answer', '',
                             'Relative error', 'Value'])
            for i in range(len(answer)):
                writer.writerow(parameters[i] + answer[i])

    @staticmethod
    def __generate_answer(algorithms: Algorithms, errors: tuple) -> tuple[list[str | Any]]:
        answer = []
        error_names = ['Greedy to maximum', 'Thrifty to minimum', 'Greedy-thrifty to maximum',
                       'Greedy-thrifty to minimum', 'Thrifty-greedy to maximum', 'Thrifty-greedy to minimum']
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
        if not os.path.exists(Paths.path_to_tmp):
            os.mkdir(Paths.path_to_tmp)
        return Paths.path_to_tmp

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
        results = []
        with open(path) as file:
            n = file.readline().strip()
            results.append(validators.Int_1_1000_Validator().validate(n, 0))

            min_a, max_a = file.readline().strip().split()
            results.append(validators.Double_0_100000_Validator().validate(min_a, 0))
            results.append(validators.Double_0_100000_Validator().validate(max_a, 0))

            is_normal = file.readline().strip()
            results.append(validators.DistributionValidator().validate(is_normal, 0))

            min_b, max_b = file.readline().strip().split()
            results.append(validators.Double_0_1_Validator().validate(min_b, 0))
            results.append(validators.Double_0_1_Validator().validate(max_b, 0))

            consider_inorganic = file.readline().strip()
            results.append(validators.InorganicValidator().validate(consider_inorganic, 0))

            t = file.readline().strip()
            results.append(validators.Int_1_1000_Validator().validate(t, 0))

        for res in results:
            if res[0] == QtGui.QValidator.State.Invalid:
                print(res)
                raise ValueError

        is_normal = 1 if is_normal.lower() in ['1', 'нормальное'] else 0

        consider_inorganic = 1 if consider_inorganic.lower() in ['1', 'да'] else 0

        return int(n), float(min_a), float(max_a), is_normal, float(min_b), float(max_b), consider_inorganic, int(t)

    @staticmethod
    def read_matrix(path: str) -> tuple[int, list[list[float]]]:
        with open(path) as file:
            n = file.readline().strip()
            if validators.Int_1_1000_Validator().validate(n, 0)[0] == QtGui.QValidator.State.Invalid:
                raise ValueError
            n = int(n)
            matrix = [[] for _ in range(n)]
            for i in range(n):
                row = file.readline().strip().split()
                if len(row) != n:
                    raise ValueError
                for element in row:
                    if validators.Double_0_100000_Validator().validate(element, 0)[0] == QtGui.QValidator.State.Invalid:
                        raise ValueError
                matrix[i] = list(map(float, row))
        return n, matrix




