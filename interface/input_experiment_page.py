from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from interface.plot_page import PlotPage
from interface.answer_page import AnswerPage
from algorithms import Algorithms
from experiment import experiment
from file_controller import FileController
from paths import Paths
from interface import validators


class InputExperimentPage(QtWidgets.QWidget):
    """Страница ввода параметров для эксперимента"""

    def __init__(self, plot_page: PlotPage, answer_page: AnswerPage):
        super(InputExperimentPage, self).__init__()
        self.plot_page = plot_page
        self.answer_page = answer_page
        self.setObjectName('InputExperimentPage')
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setMinimumSize(520, 760)
        self.setMaximumWidth(550)

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
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setText("")
        self.lineEdit_1.textChanged.connect(self.set_stage_duration)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 2, 0, 1, 1)

        self.label_20 = QtWidgets.QLabel(parent=self)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(parent=self)
        self.label_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(220, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)

        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")

        self.label_18 = QtWidgets.QLabel(parent=self)
        self.label_18.setObjectName("label_18")
        self.gridLayout_13.addWidget(self.label_18, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self)
        self.label_17.setObjectName("label_17")
        self.gridLayout_13.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(parent=self)
        self.label_19.setObjectName("label_19")
        self.gridLayout_13.addWidget(self.label_19, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self)
        self.label_16.setObjectName("label_16")
        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 4)
        self.gridLayout.addLayout(self.gridLayout_13, 8, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_13.addItem(spacerItem3, 1, 3, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_13, 8, 0, 1, 2)

        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_4 = QtWidgets.QLabel(parent=self)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self)
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_12.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_12.addWidget(self.lineEdit_3, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_12, 5, 0, 1, 2)

        spacerItem4 = QtWidgets.QSpacerItem(220, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(parent=self)
        self.label_7.setText("")
        self.label_7.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 12, 1, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem6, 9, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)

        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem7, 11, 0, 1, 1)

        self.label = QtWidgets.QLabel(parent=self)
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem8, 13, 1, 1, 1)

        self.stackedWidget = QtWidgets.QStackedWidget(parent=self)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.page_1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.set_distribution_page(1))
        self.gridLayout_19.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.page_1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.set_distribution_page(2))
        self.gridLayout_19.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(parent=self.page_1)
        self.label_23.setObjectName("label_23")
        self.gridLayout_19.addWidget(self.label_23, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_17.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.page_2)
        self.label_11.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_17.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.page_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_17.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_17.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.page_2)
        self.label_12.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_17.addWidget(self.label_12, 3, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_17.addWidget(self.lineEdit_8, 3, 1, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.set_distribution_page(0))
        self.gridLayout_17.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.gridLayout_15.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_21 = QtWidgets.QLabel(parent=self.page_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_21.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(parent=self.page_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_21.addWidget(self.label_24, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(parent=self.page_3)
        self.label_25.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_21.addWidget(self.label_25, 2, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(parent=self.page_3)
        self.label_26.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_21.addWidget(self.label_26, 3, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.page_3)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_21.addWidget(self.lineEdit_10, 2, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.page_3)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_21.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.page_3)
        self.pushButton_9.clicked.connect(lambda: self.set_distribution_page(0))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_21.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 10, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(parent=self)
        self.checkBox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 7, 0, 1, 2)

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.pushButton = QtWidgets.QPushButton(parent=self)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())

        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton.setText("")
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 12, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.setCurrentIndex(0)

        self.retranslateUi()

        self.label_back_1 = QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_back_1, 0, 0, 4, 1)

        self.label_back_2 = QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_back_2, 0, 1, 4, 1)

        self.label_back_3 = QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_back_3, 5, 0, 1, 2)

        self.label_back_4 = QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_back_4, 7, 0, 3, 2)

        self.label_back_5 = QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_back_5, 10, 0, 2, 2)

        self.showEvent = self.show_back_labels

        self.setTabOrder(self, self.lineEdit_1)
        self.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8, self.checkBox)
        self.setTabOrder(self.checkBox, self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4, self.pushButton)
        self.setTabOrder(self.pushButton, self.pushButton_4)

        self.pushButton.clicked.connect(self.run_experiment)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_1.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_20.setText(_translate("MainWindow", "One stage lasts n days"))
        self.label_20.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_20.setProperty("subheading", _translate("MainWindow", "true"))
        self.lineEdit_4.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_6.setText(
            _translate("MainWindow", "<html><head/><body><p>Number of<br>experiments</p></body></html>"))
        self.label_6.setProperty("heading", _translate("MainWindow", "true"))
        self.label_6.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_18.setText(_translate("MainWindow", "Na: 0.15 - 0.92"))
        self.label_18.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_18.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_17.setText(_translate("MainWindow", "   K: 4 - 8.7"))
        self.label_17.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_17.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_19.setText(_translate("MainWindow", "N: 1.2 - 3"))
        self.label_19.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_19.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_16.setText(_translate("MainWindow", "   Inorganics content, mol/100g"))
        self.label_16.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_16.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_4.setText(_translate("MainWindow", "max:"))
        self.label_4.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_4.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_3.setText(_translate("MainWindow", "min:"))
        self.label_3.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_3.setProperty("exp_style", _translate("MainWindow", "true"))
        self.lineEdit_2.setProperty("exp_style", _translate("MainWindow", "true"))
        self.lineEdit_3.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_7.setProperty("error", _translate("MainWindow", "true"))
        self.label_7.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_2.setText(_translate("MainWindow", "Sugar content before processing"))
        self.label_2.setProperty("heading", _translate("MainWindow", "true"))
        self.label_2.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label.setText(
            _translate("MainWindow", "<html><head/><body><p>Number of<br>beet varieties</p></body></html>"))
        self.label.setProperty("heading", _translate("MainWindow", "true"))
        self.label.setProperty("exp_style", _translate("MainWindow", "true"))
        self.pushButton_6.setText(_translate("MainWindow", "Concentrated distribution"))
        self.pushButton_8.setText(_translate("MainWindow", "Uniform distribution"))
        self.label_23.setText(_translate("MainWindow", "Distribution of degradation"))
        self.label_23.setProperty("heading", _translate("MainWindow", "true"))
        self.label_23.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_5.setText(_translate("MainWindow", "Distribution of degradation"))
        self.label_5.setProperty("heading", _translate("MainWindow", "true"))
        self.label_5.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_11.setText(_translate("MainWindow", "Minium value:"))
        self.label_11.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_11.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_14.setText(_translate("MainWindow", "Concentrated"))
        self.label_14.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_14.setProperty("heading", _translate("MainWindow", "true"))
        self.lineEdit_7.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_12.setText(_translate("MainWindow", "Maximum value:"))
        self.label_12.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_12.setProperty("subheading", _translate("MainWindow", "true"))
        self.lineEdit_8.setProperty("exp_style", _translate("MainWindow", "true"))
        self.pushButton_4.setText(_translate("MainWindow", "<"))
        self.label_21.setText(_translate("MainWindow", "Distribution of degradation"))
        self.label_21.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_21.setProperty("heading", _translate("MainWindow", "true"))
        self.label_24.setText(_translate("MainWindow", "Uniform"))
        self.label_24.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_24.setProperty("heading", _translate("MainWindow", "true"))
        self.label_25.setText(_translate("MainWindow", "Minium value:"))
        self.label_25.setProperty("exp_style", _translate("MainWindow", "true"))
        self.label_25.setProperty("subheading", _translate("MainWindow", "true"))
        self.label_26.setText(_translate("MainWindow", "Maximum value:"))
        self.label_26.setProperty("exp_style", _translate("InputExperimentPage", "true"))
        self.label_26.setProperty("subheading", _translate("InputExperimentPage", "true"))
        self.lineEdit_10.setProperty("exp_style", _translate("InputExperimentPage", "true"))
        self.lineEdit_9.setProperty("exp_style", _translate("InputExperimentPage", "true"))

        self.pushButton_9.setText(_translate("MainWindow", "<"))
        self.checkBox.setText(_translate("InputExperimentPage", "Consider the effects of inorganics"))
        self.checkBox.setProperty("exp_style", _translate("MainWindow", "true"))
        self.checkBox.setProperty("color_of_back_label", _translate("MainWindow", "red"))
        self.checkBox.setProperty("heading", _translate("InputExperimentPage", "true"))
        self.pushButton.setProperty("exp_style", _translate("InputExperimentPage", "true"))
        self.pushButton_10.setProperty("exp_style", _translate("InputExperimentPage", "true"))

    def show_back_labels(self, widget):
        self.label_back_1.setPixmap(QtGui.QPixmap(":/icons/pngs/kolichestvo_sortov.png").scaled(self.label_6.size(),
                                                                                                QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                                                                QtCore.Qt.TransformationMode.SmoothTransformation))
        self.label_back_1.lower()

        self.label_back_2.setPixmap(
            QtGui.QPixmap(":/icons/pngs/kolichestvo_experimentov.png").scaled(self.label_6.size(),
                                                                              QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                                              QtCore.Qt.TransformationMode.SmoothTransformation))
        self.label_back_2.lower()

        self.label_back_3.setPixmap(
            QtGui.QPixmap(":/icons/pngs/sakharistost.png").scaled(self.label_2.size(),
                                                                  QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                                  QtCore.Qt.TransformationMode.SmoothTransformation))
        self.label_back_3.lower()

        self.label_back_4.setPixmap(QtGui.QPixmap(Paths.path_to_inorganic_img).scaled(self.label_2.size(),
                                                                                                QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                                                                QtCore.Qt.TransformationMode.SmoothTransformation))
        self.label_back_4.lower()

        self.label_back_5.setPixmap(
            QtGui.QPixmap(Paths.path_to_distribution_img).scaled(self.label_2.size(),
                                                                 QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                                 QtCore.Qt.TransformationMode.SmoothTransformation))
        self.label_back_5.lower()

    def set_distribution_page(self, index: int):
        self.stackedWidget.setCurrentIndex(index)

        if index == 0:
            image_path = Paths.path_to_distribution_img
        elif index == 1:
            image_path = Paths.path_tu_concentrated_distribution_img
        else:
            image_path = Paths.path_to_uniform_distribution_img

        self.label_back_5.setPixmap(
            QtGui.QPixmap(image_path).scaled(self.label_2.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                             QtCore.Qt.TransformationMode.SmoothTransformation))

    def write_err_tab(self, s: str):
        self.label_7.setText(s)

    def __check_params(self, n: int, t: int, min_a: float, max_a: float,
                       min_b: float, max_b: float, is_normal: bool) -> bool:
        if min_a > max_a:
            self.write_err_tab('Min sugar content should not exceed max')
            return False

        if not (0.14 <= min_a <= 0.2) or not (0.14 <= max_a <= 0.2):
            self.write_err_tab('Min sugar content should\nbe within [0.14; 0.2]')
            return False

        if not is_normal and min_b > max_b:
            self.write_err_tab('Min degradation should not be greater than max')
            return False

        max_num_experiment = 1000000 // n ** 2
        if t > max_num_experiment:
            self.write_err_tab(f'Max number of experiments\nfor this matrix - {max_num_experiment}')
            return False
        return True

    def set_stage_duration(self):
        if self.lineEdit_1.text() == '':
            self.label_20.setText("One stage lasts n days")
        else:
            n = int(self.lineEdit_1.text())
            days = 100 // n if 100 % n == 0 else 100 // n + 1
            self.label_20.setText(f"One stage lasts {days} days")

    def run_experiment(self):
        try:
            n = int(self.lineEdit_1.text())
            min_a = float(self.lineEdit_2.text())
            max_a = float(self.lineEdit_3.text())

            cur_distribution = self.stackedWidget.currentIndex()
            if cur_distribution == 2:
                is_normal = False
            elif cur_distribution == 1:
                is_normal = True
            else:
                raise ValueError
            if is_normal:
                min_b = float(self.lineEdit_7.text())
                max_b = float(self.lineEdit_8.text())
            else:
                min_b = float(self.lineEdit_10.text())
                max_b = float(self.lineEdit_9.text())
            t = int(self.lineEdit_4.text())

            if self.checkBox.isChecked():
                organic = True
            else:
                organic = False
            self.write_err_tab("")
        except:
            self.write_err_tab("Fill in all fields with numbers")
            self.plot_page.clear_graph()
            self.answer_page.clear_answer()
            return

        if not self.__check_params(n, t, min_a, max_a, min_b, max_b, is_normal):
            self.plot_page.clear_graph()
            self.answer_page.clear_answer()
            return

        algorithms: Algorithms = experiment(n, t, min_a, max_a, min_b, max_b, organic, is_normal)
        self.plot_page.print_plots(algorithms)
        self.answer_page.print_answer(algorithms)
        errors = algorithms.calculate_error()
        FileController.tmp_save_experiment(n, t, min_a, max_a, min_b, max_b, organic, is_normal, algorithms, errors)

    def fill_params_from_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор файла', '/', '*.txt')[0]
        if path:
            info_msg = QtWidgets.QMessageBox()
            info_msg.setWindowTitle('Ввод параметров эксперимента')
            info_msg.setWindowIcon(QtGui.QIcon(Paths.path_to_logo))
            try:
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
            except ValueError:
                info_msg.setText('Неверный формат данных!')
                info_msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                info_msg.exec()
            except Exception as error:
                info_msg.setText('Произошла ошибка при вводе параметров из файла!')
                info_msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                info_msg.exec()
                print(error)

    def save_to_file(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save data', '/experiment parameters.csv',
                                                     '*.csv')[0]
        if path:
            info_msg = QtWidgets.QMessageBox()
            info_msg.setWindowTitle('Save')
            info_msg.setWindowIcon(QtGui.QIcon(Paths.path_to_logo))
            try:
                FileController.user_save_experiment(path)
                info_msg.setText('The file has been saved successfully!')
                info_msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            except Exception as error:
                info_msg.setText('An error occurred while saving the file!')
                info_msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                print(error)
            finally:
                info_msg.exec()
