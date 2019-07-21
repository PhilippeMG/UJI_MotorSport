import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 100))
        self.setWindowTitle("UJI MotorSport")
        self.setWindowIcon(QIcon("icon.ico"));

        # Add button widget
        pybutton = QPushButton('Pyqt', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(130, 30)

        # Create new action
        newAction = QAction(QIcon('export.png'), '&Exportar', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New document')
        newAction.triggered.connect(self.newCall)

        #Organizar

        # Create exit action
        exitAction = QAction(QIcon('logout.png'), '&Eixir', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Fitxer')
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)

    def openCall(self):
        print('Exportant les dades...')

    def newCall(self):
        print('New')

    def exitCall(self):
        print('Exit app')
        self.close()

    def clickMethod(self):
        print('PyQt')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )