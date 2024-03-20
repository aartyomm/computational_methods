from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
import pyqtgraph as pg
from algorithms import Algorithms
from paths import Paths
from interface.colored_axis import ColoredAxis


class PlotPage(QtWidgets.QWidget):
    """Страница отображения графика"""

    bars_color = '#FF781D'
    grid_color = '#181818'
    background_color = '#2B2B2B'
    axis_color = '#BCBCBC'
    grid_pen = pg.mkPen(color=grid_color, style=QtCore.Qt.PenStyle.DashLine)

    def __init__(self, parent: QtWidgets.QMainWindow | None = None):
        super(PlotPage, self).__init__(parent)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        # self.setStyleSheet('background-color: red')
        axis_pen = pg.mkPen(color=self.axis_color, width=2)
        self.axis_x = ColoredAxis(orientation='bottom', axisPen=axis_pen, textPen=axis_pen)
        self.axis_y = ColoredAxis(orientation='left', axisPen=axis_pen, textPen=axis_pen)

        self.setObjectName('PlotPage')
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.grid = QtWidgets.QGridLayout(self)
        self.setMinimumSize(200, 200)
        self.setMaximumSize(1000, 400)
        self.graph = pg.PlotWidget()
        self.graph.setMaximumSize(800, 400)
        self.graph.setBackground(None)
        self.graph.setAxisItems({'bottom': self.axis_x, 'left': self.axis_y})

        self.graph.setTitle(
            f'<span style="font-family:Century Gothic; font-size: 15pt; color: {self.axis_color}">'
            'Comparison of the objective function'
            '</span>'
        )
        self.graph.setLabel('left',
                            f'<font face="Century Gothic" size="5" color="{self.axis_color}">'
                            'Value of the objective function S'
                            '</font>')
        self.graph.setLabel('bottom',
                            f'<font face="Century Gothic" size="5" color="{self.axis_color}">Algorithms</font>')

        self.graph_icon = QtWidgets.QLabel()
        self.graph_icon.setObjectName('graph_icon')
        self.graph_icon.setPixmap(QtGui.QPixmap(Paths.path_to_graph_icon).scaledToWidth(256))
        self.graph_icon.setFixedSize(256, 256)
        self.grid.addWidget(self.graph_icon, 0, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.grid.addWidget(self.graph, 0, 0)
        self.graph.lower()

        self.algorithms: Algorithms | None = None
        self.x = []

    def print_plots(self, algorithms: Algorithms):
        self.graph.clear()
        self.graph_icon.setVisible(False)
        self.algorithms = algorithms
        for i in range(len(self.algorithms)):
            self.x.append((i, self.algorithms[i].name))
        self.graph.getAxis('bottom').setTicks([self.x])

        y = [algorithms[i].ans[-1] for i in range(len(algorithms))]
        x = [i for i in range(len(algorithms))]
        self.bar = pg.BarGraphItem(x=x, height=y, width=0.6, brush=self.bars_color)
        self.graph.setYRange(min(y) * 0.99, max(y) * 1.005)
        grid = pg.GridItem(textPen=None, pen=self.grid_pen)
        grid.setTickSpacing(x=[0.5], y=[None, None])
        self.graph.addItem(grid)

        self.graph.addItem(self.bar)
        for i in range(len(algorithms)):
            label = pg.TextItem(text=str(round(algorithms[i].ans[-1], 3)), color=self.grid_color)
            label.setPos(x[i], y[i])
            label.setAnchor((0.5, 0))
            self.graph.addItem(label)

    def clear_graph(self):
        self.graph_icon.setVisible(True)
        self.graph.clear()

    def change_line(self, ind: int):
        if self.line_checkboxes[ind].isChecked():
            self.print_line(ind)
        else:
            self.clear_line(ind)

    def clear_line(self, ind: int):
        self.lines[ind].setData()

    def print_line(self, ind: int):
        self.lines[ind].setData(self.x, self.algorithms[ind].ans, name=self.algorithms[ind].name, pen=self.pens[ind])
