from PyQt6 import QtWidgets
from algorithms import Algorithms
from PyQt6.QtCore import Qt
from PyQt6 import QtCore


class AnswerPage(QtWidgets.QWidget):
    NUM_ALGORITHMS = 4

    def __init__(self):
        super(AnswerPage, self).__init__()
        self.setObjectName('AnswerPage')
        self.setMaximumSize(800, 400)

        self.grid = QtWidgets.QGridLayout(self)

        self.header = QtWidgets.QLabel()
        self.header.setText("The error of the algorithms:")
        self.header.hide()
        self.grid.addWidget(self.header, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.algorithm_names = [QtWidgets.QLabel() for _ in range(self.NUM_ALGORITHMS)]
        self.algorithms_value = [QtWidgets.QLabel() for _ in range(self.NUM_ALGORITHMS)]

        for i in range(self.NUM_ALGORITHMS):
            self.grid.addWidget(self.algorithm_names[i], 1, i, Qt.AlignmentFlag.AlignCenter)
            self.grid.addWidget(self.algorithms_value[i], 2, i, Qt.AlignmentFlag.AlignCenter)

        self.conclusion_header = QtWidgets.QLabel()
        self.conclusion_header.setText("Conclusion:")
        self.conclusion_header.hide()
        self.grid.addWidget(self.conclusion_header, 3, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.conclusion = QtWidgets.QLabel()
        self.grid.addWidget(self.conclusion, 4, 0, 1, 4, Qt.AlignmentFlag.AlignCenter)

    def print_answer(self, algorithms: Algorithms):
        self.header.show()
        errors = algorithms.calculate_error()
        best_algorithm = algorithms[2]
        for i in range(self.NUM_ALGORITHMS):
            self.algorithm_names[i].setText(algorithms[i + 2].name)
            self.algorithms_value[i].setText(str(errors[i]) + '%')
            if algorithms[i + 2].ans[-1] > best_algorithm.ans[-1]:
                best_algorithm = algorithms[i + 2]

        self.conclusion_header.show()

        self.conclusion.setText(f'The best algorithm for recycling is {best_algorithm.name}.')

    def clear_answer(self):
        self.header.hide()
        for i in range(self.NUM_ALGORITHMS):
            self.algorithm_names[i].setText('')
            self.algorithms_value[i].setText('')

        self.conclusion_header.hide()
        self.conclusion.setText('')
