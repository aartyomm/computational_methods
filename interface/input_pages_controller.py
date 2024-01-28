from PyQt6 import QtWidgets
from PyQt6 import QtCore
from interface.input_matrix_page import InputMatrixPage
from interface.input_experiment_page import InputExperimentPage
from interface.plot_page import PlotPage


class InputPagesController(QtWidgets.QStackedWidget):
    """Управление страницами ввода данных"""

    def __init__(self, parent: QtWidgets.QMainWindow, plot_page: PlotPage):
        super(InputPagesController, self).__init__(parent)
        self.setGeometry(QtCore.QRect(0, 30, 400, 570))
        self.addWidget(InputMatrixPage(plot_page))
        self.addWidget(InputExperimentPage(plot_page))
        self.change_input_page(0)

    def change_input_page(self, index: int):
        self.setCurrentIndex(index)
