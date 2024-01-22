from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui


class InputMatrixPage (QtWidgets.QWidget):
    """Страница ручного ввода данных"""

    def __init__(self):
        super(InputMatrixPage, self).__init__()
        self.describe = QtWidgets.QLabel(self)
        self.describe.setGeometry(QtCore.QRect(20, 20, 30, 100))
        self.describe.setText('На этой странице будет ввод матрицы')
        font = QtGui.QFont()
        font.setPointSize(15)
        self.describe.setFont(font)
        self.describe.adjustSize()
