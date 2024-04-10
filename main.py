import sys, ctypes, os

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    myappid = 'AreteTehnology.Control.v0.2' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    window = MainWindow()
    #window.showMaximized()
    sys.exit(app.exec_())