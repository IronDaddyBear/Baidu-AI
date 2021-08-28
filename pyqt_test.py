from test import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QImage, QPixmap, QWindow
import sys

class myWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.initUI()
        self.initSlot()

    def initSlot(self):
        self.pushButton.clicked.connect(self.say)
    
    def initUI(self):
        self.win = QMainWindow()
        self.setupUi(self.win)
    
    def say(self):
        print('hello')
    
    def show(self):
        self.win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    print('started')
    # app.exec__()
    # sys.exit()