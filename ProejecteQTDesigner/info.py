import sys 
import time
from PyQt5 import uic, QtWidgets 
from PyQt5.QtWidgets import QDialog
wInici = "ajuda.ui"

# Nombre del archivo aquí. 

Ui_MainWindow, QtBaseClass = uic.loadUiType(wInici) 

class Info(QtWidgets.QMainWindow, Ui_MainWindow): 
    
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self) 
        Ui_MainWindow.__init__(self) 
        self.setupUi(self) 
       
            
            
