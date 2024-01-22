from PyQt6 import QtWidgets
from PyQt6 import QtCore
from interface.input_matrix_page import InputMatrixPage
from interface.input_experimant_page import InputExperimentPage


class InputPagesController(QtWidgets.QStackedWidget):
    """Управление страницами ввода данных"""

    def __init__(self, parent: QtWidgets.QMainWindow | None = None):
        super(InputPagesController, self).__init__(parent)
        self.setGeometry(QtCore.QRect(0, 30, 400, 600))
        self.addWidget(InputMatrixPage())
        self.addWidget(InputExperimentPage())
        self.change_input_page(0)

    def change_input_page(self, index: int):
        self.setCurrentIndex(index)
