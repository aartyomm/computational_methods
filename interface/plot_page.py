from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui


class PlotPage(QtWidgets.QWidget):
    """Страница отображения графика"""

    def __init__(self, parent: QtWidgets.QMainWindow | None = None):
        super(PlotPage, self).__init__(parent)
        self.setGeometry(QtCore.QRect(400, 0, 800, 600))
        self.describe = QtWidgets.QLabel(self)
        self.describe.setGeometry(QtCore.QRect(200, 250, 30, 100))
        self.describe.setText('Здесь будет график')
        font = QtGui.QFont()
        font.setPointSize(30)
        self.describe.setFont(font)
        self.describe.adjustSize()
