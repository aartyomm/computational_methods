from PyQt6 import QtWidgets
from interface.menu_bar import MenuBar
from interface.input_pages_controller import InputPagesController
from interface.plot_page import PlotPage


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно приложения"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1200, 600)
        self.input_pages_controller = InputPagesController(self)
        self.setMenuBar(MenuBar(self.input_pages_controller))
        self.plot_page = PlotPage(self)
