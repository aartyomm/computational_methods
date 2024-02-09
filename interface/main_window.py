from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from interface.input_pages_controller import InputPagesController
from interface.plot_page import PlotPage
from paths import Paths


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно приложения"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1600, 800)
        self.setWindowTitle('SweetBeet')
        self.setWindowIcon(QtGui.QIcon(Paths.path_to_logo))
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('MainWidget')
        self.setCentralWidget(self.central_widget)
        self.grid = QtWidgets.QGridLayout(self.central_widget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setColumnStretch(0, 6)
        self.grid.setColumnStretch(1, 9)

        self.plot_page = PlotPage()
        self.input_pages_controller = InputPagesController(self.plot_page, self)
        self.grid.addWidget(self.input_pages_controller)
        self.grid.addWidget(self.plot_page)

        with open(Paths.path_to_style, 'r') as file:
            self.setStyleSheet(file.read())
