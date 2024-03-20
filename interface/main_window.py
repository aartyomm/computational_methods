from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from interface.input_pages_controller import InputPagesController
from interface.plot_page import PlotPage
from interface.input_experiment_page import InputExperimentPage
from interface.answer_page import AnswerPage
from paths import Paths


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно приложения"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1600, 838)
        self.setWindowTitle('Educational project. Optimal schedule processing')
        self.setWindowIcon(QtGui.QIcon(Paths.path_to_logo))
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('MainWidget')
        self.central_widget.showEvent = self.showEvent = self.show_back_label
        self.setCentralWidget(self.central_widget)
        self.grid = QtWidgets.QGridLayout(self.central_widget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setColumnStretch(0, 6)
        self.grid.setColumnStretch(1, 9)

        self.plot_page = PlotPage()
        # self.input_pages_controller = InputPagesController(self.plot_page, self)
        self.answer_page = AnswerPage()
        self.input_experiment_page = InputExperimentPage(self.plot_page, self.answer_page)
        self.grid.addWidget(self.input_experiment_page, 0, 0, 2, 1)
        self.grid.addWidget(self.plot_page, 0, 1, 1, 1)
        self.grid.addWidget(self.answer_page, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.label_back = QtWidgets.QLabel()
        self.grid.addWidget(self.label_back, 0, 0, 2, 2)

        with open(Paths.path_to_style, 'r') as file:
            self.setStyleSheet(file.read())

    def show_back_label(self, widget):
        self.label_back.setPixmap(QtGui.QPixmap(":/icons/pngs/fon.png").scaled(self.central_widget.size(),
                                                                               QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                                               QtCore.Qt.TransformationMode.SmoothTransformation))
        self.label_back.lower()
