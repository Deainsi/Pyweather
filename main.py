import sys

from PyQt5 import QtWidgets

from pw import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Pyweather = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Pyweather)
    Pyweather.show()
    sys.exit(app.exec_())
