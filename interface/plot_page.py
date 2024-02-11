from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
import pyqtgraph as pg
from algorithms import Algorithms
from paths import Paths


class PlotPage(QtWidgets.QWidget):
    """Страница отображения графика"""
    pens = [
        pg.mkPen(color=QtGui.QColor('#A04D73'), width=6, style=QtCore.Qt.PenStyle.SolidLine),
        pg.mkPen(color=QtGui.QColor('#6A8DC1'), width=6, style=QtCore.Qt.PenStyle.DashLine),
        pg.mkPen(color=QtGui.QColor('#267A8B'), width=6, style=QtCore.Qt.PenStyle.DotLine),
        pg.mkPen(color=QtGui.QColor('#A3D4AF'), width=6, style=QtCore.Qt.PenStyle.DashDotLine),
        pg.mkPen(color=QtGui.QColor('#B086A8'), width=6, style=QtCore.Qt.PenStyle.DashDotDotLine),
        pg.mkPen(color=QtGui.QColor('#CDAFA5'), width=6, style=QtCore.Qt.PenStyle.DashDotLine),
    ]

    def __init__(self, parent: QtWidgets.QMainWindow | None = None):
        super(PlotPage, self).__init__(parent)

        self.setObjectName('PlotPage')
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.grid = QtWidgets.QGridLayout(self)
        self.setMinimumSize(700, 600)
        self.graph = pg.PlotWidget()
        self.graph.setBackground(None)
        self.graph.setTitle(
            '<span style="font-family:Century Gothic; font-size: 15pt; color: black">Эффективность алгоритмов</span>'
        )
        self.graph.setLabel('left', '<font face="Century Gothic" size="5" color="black">Значение целевой функции S</font>')
        self.graph.setLabel('bottom', '<font face="Century Gothic" size="5" color="black">Время</font>')

        self.legend = self.graph.addLegend(offset=(-1, -1), labelTextColor='black')
        self.legend.mouseDragEvent = lambda *args, **kwargs: None
        self.legend.hoverEvent = lambda *args, **kwargs: None

        self.vertical_for_checkboxes = QtWidgets.QVBoxLayout()
        self.vertical_for_checkboxes.setSpacing(8)
        self.vertical_for_checkboxes.addStretch()
        self.vertical_for_checkboxes.setContentsMargins(0, 0, 155, 52)

        self.horizontal_for_checkboxes = QtWidgets.QHBoxLayout(self.graph)
        self.horizontal_for_checkboxes.addStretch()
        self.horizontal_for_checkboxes.addLayout(self.vertical_for_checkboxes)

        self.graph_icon = QtWidgets.QLabel()
        self.graph_icon.setObjectName('graph_icon')
        self.graph_icon.setPixmap(QtGui.QPixmap(Paths.path_to_graph_icon).scaledToWidth(256))
        self.graph_icon.setFixedSize(256, 256)
        self.grid.addWidget(self.graph_icon, 0, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.grid.addWidget(self.graph, 0, 0)
        self.graph.lower()

        self.lines = []
        self.algorithms: Algorithms | None = None
        self.x = []
        change_funcs = [
            lambda: self.change_line(0),
            lambda: self.change_line(1),
            lambda: self.change_line(2),
            lambda: self.change_line(3),
            lambda: self.change_line(4),
            lambda: self.change_line(5),
        ]
        self.line_checkboxes: list[QtWidgets.QCheckBox] = [QtWidgets.QCheckBox() for _ in range(len(change_funcs))]
        for i in range(len(self.line_checkboxes)):
            self.line_checkboxes[i].setChecked(True)
            self.line_checkboxes[i].setVisible(False)
            self.line_checkboxes[i].stateChanged.connect(change_funcs[i])
            self.line_checkboxes[i].setProperty('plot_style', 'true')
            self.vertical_for_checkboxes.addWidget(self.line_checkboxes[i])
            self.line_checkboxes.append(self.line_checkboxes[i])

    def print_plots(self, algorithms: Algorithms):
        self.graph.clear()
        self.graph_icon.setVisible(False)
        self.lines.clear()
        self.algorithms = algorithms
        self.x = [i for i in range(1, len(algorithms[0].ans) + 1)]
        self.graph.setLayout(self.horizontal_for_checkboxes)
        for i in range(len(algorithms)):
            self.line_checkboxes[i].setVisible(True)
            if self.line_checkboxes[i].isChecked():
                self.lines.append(self.graph.plot(self.x, algorithms[i].ans, name=algorithms[i].name, pen=self.pens[i]))
            else:
                self.lines.append(self.graph.plot([], [], name=algorithms[i].name, pen=self.pens[   i]))

    def clear_graph(self):
        self.graph_icon.setVisible(True)
        self.lines.clear()
        self.graph.clear()
        for checkbox in self.line_checkboxes:
            checkbox.setVisible(False)

    def change_line(self, ind: int):
        if self.line_checkboxes[ind].isChecked():
            self.print_line(ind)
        else:
            self.clear_line(ind)

    def clear_line(self, ind: int):
        self.lines[ind].setData()

    def print_line(self, ind: int):
        self.lines[ind].setData(self.x, self.algorithms[ind].ans, name=self.algorithms[ind].name, pen=self.pens[ind])
