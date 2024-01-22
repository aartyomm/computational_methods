from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from interface.input_pages_controller import InputPagesController


class MenuBar(QtWidgets.QMenuBar):
    """Меню, находящееся сверху"""

    def __init__(self, pages_controller: InputPagesController):
        super(MenuBar, self).__init__()
        self.setGeometry(QtCore.QRect(0, 0, 1200, 25))

        self.matrix_action = QtGui.QAction(self)
        self.matrix_action.setText('Ручной ввод')
        self.experiment_action = QtGui.QAction(self)
        self.experiment_action.setText('Эксперимент')

        self.addAction(self.matrix_action)
        self.addAction(self.experiment_action)
        self.matrix_action.triggered.connect(lambda: pages_controller.change_input_page(0))
        self.experiment_action.triggered.connect(lambda: pages_controller.change_input_page(1))
