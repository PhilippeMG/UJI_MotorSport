import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QProgressBar, \
    QMainWindow
from PyQt5.QtGui import QIcon

#https://doc.qt.io/qt-5/stylesheet-examples.html
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'UJI MotorSport'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("icon.ico"));


        windowLayout = QVBoxLayout()
        windowLayout.addWidget(QLabel("Primer"))

        self.setLayout(windowLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
