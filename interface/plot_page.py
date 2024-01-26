from PyQt6 import QtWidgets
from PyQt6 import QtCore
import pyqtgraph as pg
from algorithms import Algorithms
from experiment import experiment


class PlotPage(QtWidgets.QWidget):
    """Страница отображения графика"""

    pens = [
        pg.mkPen(color='red', width=1, style=QtCore.Qt.PenStyle.DashLine),
        pg.mkPen(color='blue', width=2, style=QtCore.Qt.PenStyle.SolidLine),
        pg.mkPen(color='cyan', width=2, style=QtCore.Qt.PenStyle.DotLine),
        pg.mkPen(color='green', width=2, style=QtCore.Qt.PenStyle.DashDotLine),
        pg.mkPen(color='magenta', width=2, style=QtCore.Qt.PenStyle.DashDotDotLine),
        pg.mkPen(color='darkGreen', width=2, style=QtCore.Qt.PenStyle.DashDotLine),
    ]

    checkboxes_coords = [
        QtCore.QPoint(600, 377),
        QtCore.QPoint(600, 400),
        QtCore.QPoint(600, 425),
        QtCore.QPoint(600, 446),
        QtCore.QPoint(600, 471),
        QtCore.QPoint(600, 495),
    ]

    def __init__(self, parent: QtWidgets.QMainWindow | None = None):
        super(PlotPage, self).__init__(parent)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.setGeometry(QtCore.QRect(400, 20, 800, 580))

        self.graph = pg.PlotWidget()
        self.graph.setBackground('w')
        self.graph.setTitle('Эффективность алгоритмов', color='black', size='15pt')
        self.graph.setLabel('left', 'S', color='black')
        self.graph.setLabel('bottom', 'Время', color='black')

        self.legend = self.graph.addLegend(offset=(575, 330))
        self.legend.mouseDragEvent = lambda *args, **kwargs: None
        self.legend.hoverEvent = lambda *args, **kwargs: None

        self.grid_layout.addWidget(self.graph)

        self.lines = []
        self.line_checkboxes: list[QtWidgets.QCheckBox] = []
        self.algorithms: Algorithms | None = None
        self.x = []

    def print_plots(self, algorithms: Algorithms):
        self.graph.clear()
        self.lines.clear()
        if len(self.line_checkboxes) == 0:
            change_funcs = [
                lambda: self.change_line(0),
                lambda: self.change_line(1),
                lambda: self.change_line(2),
                lambda: self.change_line(3),
                lambda: self.change_line(4),
                lambda: self.change_line(5),
            ]

            for i in range(len(algorithms)):
                cur_checkbox = QtWidgets.QCheckBox(self)
                cur_checkbox.move(self.checkboxes_coords[i])
                cur_checkbox.setChecked(True)
                cur_checkbox.show()
                cur_checkbox.stateChanged.connect(change_funcs[i])
                self.line_checkboxes.append(cur_checkbox)

        self.algorithms = algorithms
        self.x = [i for i in range(1, len(algorithms[0].ans) + 1)]
        for i in range(len(algorithms)):
            if self.line_checkboxes[i].isChecked():
                self.lines.append(self.graph.plot(self.x, algorithms[i].ans, name=algorithms[i].name, pen=self.pens[i]))
            else:
                self.lines.append(self.graph.plot([], [], name=algorithms[i].name, pen=self.pens[i]))

    def change_line(self, ind: int):
        if self.line_checkboxes[ind].isChecked():
            self.print_line(ind)
        else:
            self.clear_line(ind)

    def clear_line(self, ind: int):
        self.lines[ind].setData()

    def print_line(self, ind: int):
        self.lines[ind].setData(self.x, self.algorithms[ind].ans, name=self.algorithms[ind].name, pen=self.pens[ind])
