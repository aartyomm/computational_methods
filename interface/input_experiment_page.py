from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from interface.plot_page import PlotPage
from algorithms import Algorithms
from experiment import experiment
from file_controller import FileController


class InputExperimentPage(QtWidgets.QWidget):
    """Страница ввода параметров для эксперимента"""

    def __init__(self, plot_page: PlotPage):
        super(InputExperimentPage, self).__init__()
        self.plot_page = plot_page
        self.setObjectName('InputExperimentPage')

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        self.gridLayout_8 = QtWidgets.QGridLayout(self)
        self.gridLayout_8.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 23, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_4.textChanged.connect(self.clear_answers_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 19, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_3.textChanged.connect(self.clear_answers_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_1.textChanged.connect(self.clear_answers_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_2.textChanged.connect(self.clear_answers_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self)
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(parent=self)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.toggled.connect(self.clear_answers_tab)
        self.gridLayout.addWidget(self.radioButton_1, 10, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.clear_answers_tab)
        self.gridLayout.addWidget(self.checkBox, 16, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem3, 21, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self)
        self.label_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 19, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem4, 18, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 23, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(parent=self)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setLineWidth(1)
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 20, 0, 1, 2)
        self.line_8 = QtWidgets.QFrame(parent=self)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 17, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(parent=self)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 6, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(parent=self)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)
        self.line_6 = QtWidgets.QFrame(parent=self)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 14, 0, 1, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.clear_answers_tab)
        self.gridLayout.addWidget(self.radioButton_2, 9, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self)
        self.label_11.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.lineEdit_8, 12, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self)
        self.label_12.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_7.textChanged.connect(self.clear_answers_tab)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.lineEdit_7, 11, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self)
        self.pushButton_6.clicked.connect(self.fill_params_from_file)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 22, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(parent=self)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 17, 0, 1, 2)
        self.line_10 = QtWidgets.QFrame(parent=self)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setLineWidth(1)
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 20, 0, 1, 2)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ans_label_1 = QtWidgets.QLabel(parent=self)
        self.ans_label_1.setText("")
        self.ans_label_1.setObjectName("ans_label_1")
        self.gridLayout_4.addWidget(self.ans_label_1, 0, 0, 1, 1)
        self.ans_label_11 = QtWidgets.QLabel(parent=self)
        self.ans_label_11.setText("")
        self.ans_label_11.setObjectName("ans_label_11")
        self.gridLayout_4.addWidget(self.ans_label_11, 2, 3, 1, 1)
        self.ans_label_12 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label_12.sizePolicy().hasHeightForWidth())
        self.ans_label_12.setSizePolicy(sizePolicy)
        self.ans_label_12.setText("")
        self.ans_label_12.setObjectName("ans_label_12")
        self.gridLayout_4.addWidget(self.ans_label_12, 2, 4, 1, 1)
        self.ans_label_8 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label_8.sizePolicy().hasHeightForWidth())
        self.ans_label_8.setSizePolicy(sizePolicy)
        self.ans_label_8.setText("")
        self.ans_label_8.setObjectName("ans_label_8")
        self.gridLayout_4.addWidget(self.ans_label_8, 1, 4, 1, 1)
        self.ans_label_2 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label_2.sizePolicy().hasHeightForWidth())
        self.ans_label_2.setSizePolicy(sizePolicy)
        self.ans_label_2.setText("")
        self.ans_label_2.setObjectName("ans_label_2")
        self.gridLayout_4.addWidget(self.ans_label_2, 0, 1, 1, 1)
        self.ans_label_4 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label_4.sizePolicy().hasHeightForWidth())
        self.ans_label_4.setSizePolicy(sizePolicy)
        self.ans_label_4.setText("")
        self.ans_label_4.setObjectName("ans_label_4")
        self.gridLayout_4.addWidget(self.ans_label_4, 0, 4, 1, 1)
        self.ans_label_6 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label_6.sizePolicy().hasHeightForWidth())
        self.ans_label_6.setSizePolicy(sizePolicy)
        self.ans_label_6.setText("")
        self.ans_label_6.setObjectName("ans_label_6")
        self.gridLayout_4.addWidget(self.ans_label_6, 1, 1, 1, 1)
        self.ans_label_9 = QtWidgets.QLabel(parent=self)
        self.ans_label_9.setText("")
        self.ans_label_9.setObjectName("ans_label_9")
        self.gridLayout_4.addWidget(self.ans_label_9, 2, 0, 1, 1)
        self.ans_label_5 = QtWidgets.QLabel(parent=self)
        self.ans_label_5.setText("")
        self.ans_label_5.setObjectName("ans_label_5")
        self.gridLayout_4.addWidget(self.ans_label_5, 1, 0, 1, 1)
        self.ans_label_7 = QtWidgets.QLabel(parent=self)
        self.ans_label_7.setText("")
        self.ans_label_7.setObjectName("ans_label_7")
        self.gridLayout_4.addWidget(self.ans_label_7, 1, 3, 1, 1)
        self.ans_label_10 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label_10.sizePolicy().hasHeightForWidth())
        self.ans_label_10.setSizePolicy(sizePolicy)
        self.ans_label_10.setText("")
        self.ans_label_10.setObjectName("ans_label_10")
        self.gridLayout_4.addWidget(self.ans_label_10, 2, 1, 1, 1)
        self.ans_label_3 = QtWidgets.QLabel(parent=self)
        self.ans_label_3.setText("")
        self.ans_label_3.setObjectName("ans_label_3")
        self.gridLayout_4.addWidget(self.ans_label_3, 0, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setVisible(False)
        self.gridLayout_4.addWidget(self.pushButton_4, 3, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.retranslateUi(self)

        self.setTabOrder(self, self.lineEdit_1)
        self.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3, self.radioButton_2)
        self.setTabOrder(self.radioButton_2, self.radioButton_1)
        self.setTabOrder(self.radioButton_1, self.lineEdit_7)
        self.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8, self.checkBox)
        self.setTabOrder(self.checkBox, self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4, self.pushButton)
        self.setTabOrder(self.pushButton, self.pushButton_4)

        self.radioButton_2.clicked.connect(self.show_normal_params)
        self.radioButton_1.clicked.connect(self.show_uniform_params)
        self.pushButton.clicked.connect(self.run_experiment)
        self.pushButton_4.clicked.connect(self.save_to_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("InputExperimentPage", "Свёкла"))
        self.pushButton.setText(_translate("InputExperimentPage", "Рассчитать"))
        self.pushButton_6.setText(_translate("MainWindow", "Загрузить данные из файла"))
        self.label.setText(_translate("InputExperimentPage", "Количество сортов свёклы"))
        self.label.setProperty("heading", _translate("InputExperimentPage", "true"))
        self.label_2.setText(_translate("InputExperimentPage", "Сахаристость до переработки"))
        self.label_2.setProperty("heading", _translate("InputExperimentPage", "true"))
        self.label_5.setText(_translate("InputExperimentPage", "Распределение деградации"))
        self.label_5.setProperty("heading", _translate("InputExperimentPage", "true"))
        self.label_4.setText(_translate("InputExperimentPage", "Максимальное значение:"))
        self.label_4.setProperty("subheading", _translate("InputExperimentPage", "true"))
        self.label_3.setText(_translate("InputExperimentPage", "Минимальное значение:"))
        self.label_3.setProperty("subheading", _translate("InputExperimentPage", "true"))
        self.radioButton_1.setText(_translate("InputExperimentPage", "Равномерное"))
        self.checkBox.setText(_translate("InputExperimentPage", "Учитывать влияние неорганики"))
        self.label_6.setText(_translate("InputExperimentPage", "Количество экспериментов"))
        self.label_6.setProperty("heading", _translate("InputExperimentPage", "true"))
        self.label_7.setProperty("error", _translate("InputExperimentPage", "true"))
        self.radioButton_2.setText(_translate("InputExperimentPage", "Нормальное"))
        self.label_11.setText(_translate("InputExperimentPage", "Среднее значение:"))
        self.label_12.setText(_translate("InputExperimentPage", "Отклонение:"))
        self.pushButton_4.setText(_translate("InputExperimentPage", "Сохранить"))

    def write_answers(self, algorithms: Algorithms):
        self.pushButton_4.setVisible(True)
        name_labels = [self.ans_label_1, self.ans_label_3, self.ans_label_5,
                       self.ans_label_7, self.ans_label_9, self.ans_label_11]

        value_labels = [self.ans_label_2, self.ans_label_4, self.ans_label_6,
                        self.ans_label_8, self.ans_label_10, self.ans_label_12]

        for i in range(len(name_labels)):
            name_labels[i].setText(algorithms[i].name + ':')
            value_labels[i].setText(str(round(algorithms[i].ans[-1], 2)))

    def clear_answers_tab(self):
        self.pushButton_4.setVisible(False)
        self.plot_page.clear_graph()
        labels = [self.ans_label_1, self.ans_label_2, self.ans_label_3, self.ans_label_4,
                  self.ans_label_5, self.ans_label_6, self.ans_label_7, self.ans_label_8,
                  self.ans_label_9, self.ans_label_10, self.ans_label_11, self.ans_label_12]

        for label in labels:
            label.setText('')

    def show_normal_params(self):
        self.label_11.setText("Среднее значение:")
        self.label_12.setText("Отклонение:")

    def show_uniform_params(self):
        self.label_11.setText("Минимальное значение:")
        self.label_12.setText("Максимальное значение:")

    def write_err_tab(self, s: str):
        self.label_7.setText(s)

    def run_experiment(self):
        fl = 0
        n = -1
        min_a = -1.0
        max_a = -1.0
        is_normal = False
        organic = False
        min_b = -1
        max_b = -1
        t = -1

        try:
            n = int(self.lineEdit_1.text())
            min_a = float(self.lineEdit_2.text())
            max_a = float(self.lineEdit_3.text())
            min_b = float(self.lineEdit_7.text())
            max_b = float(self.lineEdit_8.text())
            t = int(self.lineEdit_4.text())
            fl = 0
            self.write_err_tab("")
        except:
            fl = 1
            self.write_err_tab("Заполните все поля числами")

        if self.radioButton_1.isChecked():
            is_normal = False
        if self.radioButton_2.isChecked():
            is_normal = True

        if self.checkBox.isChecked():
            organic = True
        else:
            organic = False
        # line4 = int(ui.lineEdit_4.text())
        if fl == 0:
            algorithms: Algorithms = experiment(n, t, min_a, max_a, min_b, max_b, organic, is_normal)
            self.write_answers(algorithms)
            self.plot_page.print_plots(algorithms)
            errors = algorithms.calculate_error()
            FileController.tmp_save(n, t, min_a, max_a, min_b, max_b, organic, is_normal, algorithms, errors)
        if fl == 1:
            self.clear_answers_tab()

    def fill_params_from_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор файла', '/', '*.txt')[0]
        try:
            if path:
                params = FileController.read_experiment_params(path)
                self.lineEdit_1.setText(str(params[0]))
                self.lineEdit_2.setText(str(params[1]))
                self.lineEdit_3.setText(str(params[2]))
                if params[3]:
                    self.radioButton_2.setChecked(True)
                else:
                    self.radioButton_1.setChecked(True)
                self.lineEdit_7.setText(str(params[4]))
                self.lineEdit_8.setText(str(params[5]))
                if params[6]:
                    self.checkBox.setChecked(True)
                else:
                    self.checkBox.setChecked(False)
                self.lineEdit_4.setText(str(params[7]))
        except Exception as error:
            print(error)

    def save_to_file(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить данные', '/параметры эксперимента.csv',
                                                     '*.csv')[0]
        if path:
            info_msg = QtWidgets.QMessageBox()
            info_msg.setWindowTitle('Сохранение')
            try:
                FileController.user_save(path)
                info_msg.setText('Файл успешно сохранен!')
                info_msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            except Exception as error:
                info_msg.setText('Произошла ошибка при сохранении файла!')
                info_msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                print(error)
            finally:
                info_msg.exec()
