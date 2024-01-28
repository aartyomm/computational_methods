from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from interface.plot_page import PlotPage


class InputExperimentPage(QtWidgets.QWidget):
    """Страница ввода параметров для эксперимента"""

    def __init__(self, plot_page: PlotPage):
        super(InputExperimentPage, self).__init__()
        self.describe = QtWidgets.QLabel(self)
        self.describe.setGeometry(QtCore.QRect(20, 20, 30, 100))
        self.plot_page = plot_page
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setColumnStretch(0, 4)
        for i in range(1, 5):
            self.grid.setColumnStretch(i, 3)
        self.grid.setColumnStretch(5, 4)

        self.num_sorts_label = QtWidgets.QLabel()
        self.num_sorts_label.setText('Количество сортов свёклы')
        self.grid.addWidget(self.num_sorts_label, 0, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.num_sorts_input = QtWidgets.QLineEdit()
        self.num_sorts_input.setMaximumWidth(50)
        self.grid.addWidget(self.num_sorts_input, 1, 2, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.range_a_label = QtWidgets.QLabel()
        self.range_a_label.setText('Диапазон сахаристости до переработки')
        self.grid.addWidget(self.range_a_label, 2, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.min_a_label = QtWidgets.QLabel()
        self.min_a_label.setText('мин')
        self.grid.addWidget(self.min_a_label, 3, 1, Qt.AlignmentFlag.AlignCenter)

        self.min_a_input = QtWidgets.QLineEdit()
        self.min_a_input.setMaximumWidth(40)
        self.grid.addWidget(self.min_a_input, 3, 2, Qt.AlignmentFlag.AlignLeft)

        self.max_a_label = QtWidgets.QLabel()
        self.max_a_label.setText('макс')
        self.grid.addWidget(self.max_a_label, 3, 3, Qt.AlignmentFlag.AlignCenter)

        self.max_a_input = QtWidgets.QLineEdit()
        self.max_a_input.setMaximumWidth(40)
        self.grid.addWidget(self.max_a_input, 3, 4, Qt.AlignmentFlag.AlignLeft)

        self.distribution_label = QtWidgets.QLabel()
        self.distribution_label.setText('Распределение деградации')
        self.grid.addWidget(self.distribution_label, 4, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.uniform_btn = QtWidgets.QPushButton()
        self.uniform_btn.setText('Равномерное')
        self.uniform_btn.setCheckable(True)
        self.uniform_btn.setChecked(True)
        self.uniform_btn.clicked.connect(lambda: self.change_distribution_params(0))
        self.grid.addWidget(self.uniform_btn, 5, 1, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.normal_btn = QtWidgets.QPushButton()
        self.normal_btn.setText('Нормальное')
        self.normal_btn.setCheckable(True)
        self.normal_btn.clicked.connect(lambda: self.change_distribution_params(1))
        self.grid.addWidget(self.normal_btn, 5, 3, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.distrib_btn_group = QtWidgets.QButtonGroup()
        self.distrib_btn_group.addButton(self.uniform_btn)
        self.distrib_btn_group.addButton(self.normal_btn)

        self.distribution_params = QtWidgets.QStackedWidget()
        self.grid.addWidget(self.distribution_params, 6, 1, 1, 4, Qt.AlignmentFlag.AlignVCenter)

        self.uniform_params = QtWidgets.QWidget()
        self.uniform_grid = QtWidgets.QGridLayout(self.uniform_params)

        self.min_b_label = QtWidgets.QLabel()
        self.min_b_label.setText('мин')
        self.uniform_grid.addWidget(self.min_b_label, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.min_b_input = QtWidgets.QLineEdit()
        self.min_b_input.setMaximumWidth(40)
        self.uniform_grid.addWidget(self.min_b_input, 0, 1, Qt.AlignmentFlag.AlignLeft)

        self.max_b_label = QtWidgets.QLabel()
        self.max_b_label.setText('макс')
        self.uniform_grid.addWidget(self.max_b_label, 0, 2, Qt.AlignmentFlag.AlignCenter)

        self.max_b_input = QtWidgets.QLineEdit()
        self.max_b_input.setMaximumWidth(40)
        self.max_b_input.setContentsMargins(0, 0, 3, 0)
        self.uniform_grid.addWidget(self.max_b_input, 0, 3, Qt.AlignmentFlag.AlignCenter)

        self.distribution_params.addWidget(self.uniform_params)

        self.normal_params = QtWidgets.QWidget()
        self.normal_grid = QtWidgets.QGridLayout(self.normal_params)

        self.avg_label = QtWidgets.QLabel()
        self.avg_label.setText('Среднее значение')
        self.normal_grid.addWidget(self.avg_label, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.avg_input = QtWidgets.QLineEdit()
        self.avg_input.setMaximumWidth(40)
        self.normal_grid.addWidget(self.avg_input, 0, 1)

        self.deviation_label = QtWidgets.QLabel()
        self.deviation_label.setText('Отклонение')
        self.normal_grid.addWidget(self.deviation_label, 1, 0, Qt.AlignmentFlag.AlignCenter)

        self.deviation_input = QtWidgets.QLineEdit()
        self.deviation_input.setMaximumWidth(40)
        self.normal_grid.addWidget(self.deviation_input, 1, 1)

        self.distribution_params.addWidget(self.normal_params)

        self.inorganic_influence_checkbox = QtWidgets.QCheckBox()
        self.inorganic_influence_checkbox.setText('Учитывать влияние неорганики')
        self.inorganic_influence_checkbox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.grid.addWidget(self.inorganic_influence_checkbox, 7, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.num_tests_label = QtWidgets.QLabel()
        self.num_tests_label.setText('Количество экспериментов')
        self.grid.addWidget(self.num_tests_label, 8, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.num_tests_input = QtWidgets.QLineEdit()
        self.num_tests_input.setMaximumWidth(50)
        self.grid.addWidget(self.num_tests_input, 9, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.experiment_btn = QtWidgets.QPushButton()
        self.experiment_btn.setText('Рассчитать')
        self.grid.addWidget(self.experiment_btn, 10, 1, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.answer_widget = QtWidgets.QWidget()
        self.grid.addWidget(self.answer_widget, 11, 1, 6, 6)

    def change_distribution_params(self, ind: int):
        self.distribution_params.setCurrentIndex(ind)
