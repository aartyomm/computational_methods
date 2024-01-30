from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from interface.plot_page import PlotPage


class InputMatrixPage (QtWidgets.QWidget):
    """Страница ручного ввода данных"""

    def __init__(self, plot_page: PlotPage):
        super(InputMatrixPage, self).__init__()
        self.plot_page = plot_page
        self.setObjectName("InputMatrixPage")

        self.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(parent=self)
        self.label_8.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label_8.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_5)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButton_2)
        self.label_9 = QtWidgets.QLabel(parent=self)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem7)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setVisible(False)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButton_3)
        self.label_10 = QtWidgets.QLabel(parent=self)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("InputMatrixPage", "Количество сортов свёклы"))
        self.label_8.setProperty("heading", _translate("InputMatrixPage", "true"))
        self.pushButton_2.setText(_translate("InputMatrixPage", "Ввод"))
        self.label_9.setProperty("error", _translate("InputMatrixPage", "true"))
        self.pushButton_3.setText(_translate("InputMatrixPage", "Рассчитать"))
        self.label_10.setProperty("error", _translate("InputMatrixPage", "true"))

    def write_err_tab_2(self, s: str):
        self.label_9.setText(s)

    def write_err_2_tab_2(self, s: str):
        self.label_10.setText(s)
