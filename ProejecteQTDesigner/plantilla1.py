import sys 
import time
from PyQt5 import uic, QtWidgets 
from PyQt5.QtWidgets import QDialog
import info 

wInici = "plantilla2.ui"

# Nombre del archivo aquí. 

Ui_MainWindow, QtBaseClass = uic.loadUiType(wInici) 

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 
    
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self) 
        Ui_MainWindow.__init__(self) 
        self.setupUi(self) 
        self.botton.clicked.connect(self.incrementar)
        self.close.triggered.connect(self.tancant)
        self.info.triggered.connect(self.inform)
        self.alerta.setVisible(False)


    def incrementar(self):
        j=250
        for i in range(2):
                    self.barRpm.setFormat(str(j)+' Rpm')
                    self.barRpm.setValue(j) 
                    self.estadoAlerta(j )
                    print(j)

                    time.sleep(0.05)
                    j=j+200
                    
                    
    def estadoAlerta(self,valor):
        if(valor>=250):
            self.alerta.setVisible(True)
            print("Activado")

        else:
            self.alerta.setVisible(False)
            print("Desactivado")

        
    def inform(self):
        print("Informació del programa...")
        #info.llamar(self)
        wHelp= info.Info()
        wHelp.show()
    
        wHelp.exec()
  


        
    def tancant(self):
        print("Exint del programa...")
        sys.exit()
        
        
        
if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    window = MyApp() 
    window.show() 
    sys.exit(app.exec_())
#barRpm
#QProgressBar::chunk { background-color: #fffd0a;  margin: 0.5px;}  QProgressBar {text-align: center;}
