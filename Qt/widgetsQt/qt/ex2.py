import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QProgressBar, \
    QMainWindow, QPushButton, QAction

#https://pythonspot.com/pyqt5-grid-layout/
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("UJI MotoSport")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))



        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.sms)
        fileMenu.addAction(exitButton)

        self.home()

    def home(self):
        btn= QPushButton("button",self)
        btn.clicked.connect(self.sms)
        self.show()

    def sms(self):
        print("Presionado el boton")
def run():
    app = QApplication(sys.argv)
    GUI= Window()
    sys.exit(app.exec_())

run()