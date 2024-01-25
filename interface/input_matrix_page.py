from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from interface.plot_page import PlotPage
import algorithms as alg


class InputMatrixPage (QtWidgets.QWidget):
    """Страница ручного ввода данных"""
    algorithms = [
        alg.Algorithm('Венгерский мин', alg.hungarian_min),
        alg.Algorithm('Венгерский макс', alg.hungarian_max),
        alg.Algorithm('Жадный', alg.greedy_max),
        alg.Algorithm('Бережливый', alg.greedy_min),
        alg.Algorithm('Жадно-бережливый', alg.greedy_thrifty),
        alg.Algorithm('Бережливо-жадный', alg.thrifty_greedy)
    ]

    def __init__(self, plot_page: PlotPage):
        super(InputMatrixPage, self).__init__()
        self.describe = QtWidgets.QLabel(self)
        self.describe.setGeometry(QtCore.QRect(20, 20, 30, 100))
        self.plot_page = plot_page

        self.describe.setText('На этой странице будет ввод матрицы')
        font = QtGui.QFont()
        font.setPointSize(15)
        self.describe.setFont(font)
        self.describe.adjustSize()
