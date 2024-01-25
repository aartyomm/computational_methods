from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from interface.plot_page import PlotPage


class InputExperimentPage(QtWidgets.QWidget):
    """Страница ввода параметров для эксперимента"""

    def __init__(self, plot_page: PlotPage):
        super(InputExperimentPage, self).__init__()
        self.describe = QtWidgets.QLabel(self)
        self.describe.setGeometry(QtCore.QRect(20, 20, 30, 100))
        self.plot_page = plot_page

        self.describe.setText('На этой странице будет ввод параметров для тестов')
        font = QtGui.QFont()
        font.setPointSize(15)
        self.describe.setFont(font)
        self.describe.adjustSize()