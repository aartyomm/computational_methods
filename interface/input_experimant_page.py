from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui


class InputExperimentPage(QtWidgets.QWidget):
    """Страница ввода параметров для эксперимента"""

    def __init__(self):
        super(InputExperimentPage, self).__init__()
        self.describe = QtWidgets.QLabel(self)
        self.describe.setGeometry(QtCore.QRect(20, 20, 30, 100))
        self.describe.setText('На этой странице будет ввод параметров для тестов')
        font = QtGui.QFont()
        font.setPointSize(15)
        self.describe.setFont(font)
        self.describe.adjustSize()
