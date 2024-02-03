import csv
from algorithms import Algorithms
import os
import shutil


class FileController:
    tmp_path: str | None = None

    @staticmethod
    def save_experiment_result(path: str, n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float,
                               consider_inorganic: bool, is_normal: bool, algorithms: Algorithms, errors: tuple):
        with open(path, mode='w') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerow(['Параметры', 'Значение', '', 'Алгоритм', 'Результат', '',
                             'Относительная погрешность', 'Значение'])

            writer.writerow(['n', n, '', 'Венгерский мин', round(algorithms[1].ans[-1], 2), '',
                             'Жадный к максимуму', f'{errors[0]}%'])

            writer.writerow(['t', t, '', 'Венгерский макс', round(algorithms[0].ans[-1], 2), '',
                             'Бережливый к минимуму', f'{errors[1]}%'])

            writer.writerow(['a', f'[{min_a}; {max_a}]', '', 'Жадный', round(algorithms[2].ans[-1], 2), '',
                             'Жадно-бережливый к максимуму', f'{errors[2]}%'])

            writer.writerow(['Распределение b', 'Нормальное' if is_normal else 'Равномерное', '', 'Бережливый',
                             round(algorithms[3].ans[-1], 2), '', ' Жадно-бережливый к минимуму', f'{errors[3]}%'])

            if is_normal:
                writer.writerow(['b', f'a={min_b}; b={max_b}', '', 'Жадно-бережливый',
                                 round(algorithms[4].ans[-1], 2), '', 'Бережливо-Жадный к максимуму', f'{errors[4]}%'])
            else:
                writer.writerow(['b', f'[{min_b}; {max_b}]', '', 'Жадно-бережливый', round(algorithms[4].ans[-1], 2),
                                 '', 'Бережливо-Жадный к максимуму', f'{errors[4]}%'])

            writer.writerow(['Влияние неорганики', 'Да' if consider_inorganic else 'Нет', '', 'Бережливо-Жадный',
                             round(algorithms[5].ans[-1], 2), '', 'Бережливо-Жадный к минимуму', f'{errors[5]}%'])

    @staticmethod
    def tmp_save(n: int, t: int, min_a: float, max_a: float, min_b: float, max_b: float,
                 consider_inorganic: bool, is_normal: bool, algorithms: Algorithms, errors: tuple):
        if FileController.tmp_path is None:
            path_to_dir = os.getcwd() + '/tmp'
            if not os.path.exists(path_to_dir):
                os.mkdir(path_to_dir)
            FileController.tmp_path = path_to_dir + '/tmp.csv'

        FileController.save_experiment_result(FileController.tmp_path, n, t, min_a, max_a, min_b, max_b,
                                              consider_inorganic, is_normal, algorithms, errors)

    @staticmethod
    def user_save(user_path: str):
        return shutil.copy(FileController.tmp_path, user_path)

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




