import sys
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from interface.main_window import MainWindow
from resources import resource

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont(':/fonts/fonts/GOTHIC_regular.TTF')
    QtGui.QFontDatabase.addApplicationFont(':/fonts/fonts/GOTHICB_bold.TTF')
    QtGui.QFontDatabase.addApplicationFont(':/fonts/fonts/GOTHICBI_bold_italic.TTF')
    QtGui.QFontDatabase.addApplicationFont(':/fonts/GOTHICI_italic.TTF')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
