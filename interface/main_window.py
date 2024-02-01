from PyQt6 import QtWidgets
from interface.input_pages_controller import InputPagesController
from interface.plot_page import PlotPage


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно приложения"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1600, 800)
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid = QtWidgets.QGridLayout(self.central_widget)
        self.grid.setColumnStretch(0, 6)
        self.grid.setColumnStretch(1, 9)

        self.plot_page = PlotPage()
        self.input_pages_controller = InputPagesController(self.plot_page, self)
        self.grid.addWidget(self.input_pages_controller)
        self.grid.addWidget(self.plot_page)

        with open('interface/style.qss', 'r') as file:
            self.setStyleSheet(file.read())
