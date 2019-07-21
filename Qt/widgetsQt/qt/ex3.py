import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QProgressBar


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.tablaCluster()
        self.show()


    def tablaCluster(self):
        self.horizontalGroupBox = QGroupBox("Prototipo en Qt5 v1.0")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        pbTemp = QProgressBar(self)
        pbTemp.setFixedWidth(500)

        pbTemp.setStyleSheet(
            "QProgressBar::chunk { background-color: #0b8ce8;  margin: 0.5px;}  QProgressBar {text-align: center;}")  # change text color
        # pbTemp.setStyleSheet("QProgressBar {text-align: center;}") #change text color
        # pbTemp.setStyleSheet("color: rgb(28, 43, 255);") #change text color
        # pbTemp.setTextVisible(False)
        pbTemp.setValue(40)

        pbTemp.setFormat(str(pbTemp.value()) + ' º C')

        pbRev = QProgressBar(self)
        pbRev.setStyleSheet(
            "QProgressBar::chunk { background-color: #fffd0a;  margin: 0.5px;}  QProgressBar {text-align: center;}")  # change text color
        # pbRev.setStyleSheet("QProgressBar::chunk {    background-color:#fffd00;    width: 10px;    margin: 0.5px;} QProgressBar {text-align: center;}")
        pbRev.setFixedWidth(500)

        pbRev.setGeometry(30, 40, 200, 25)
        pbRev.setValue(20)
        pbRev.setFormat(str(pbRev.value()) + ' Rpm')

        pbVel = QProgressBar(self)
        pbVel.setStyleSheet(
            "QProgressBar::chunk { background-color: #ff9d00;  margin: 0.5px;}  QProgressBar {text-align: center;}")  # change text color

        # pbVel.setStyleSheet("QProgressBar {     border: 6px solid pink;     border-radius: 5px; text-align: center;}  QProgressBar::chunk {     background-color: #35ec00;   margin: 1px;   width: 20px; }")
        pbVel.setFixedWidth(500)

        pbVel.setGeometry(30, 40, 20, 25)
        pbVel.setValue(60)
        pbVel.setFormat(str(pbVel.value()) + ' K/h')

        layout.addWidget(QLabel('Velocidad'), 0, 0)
        layout.addWidget(pbVel, 0, 1)

        layout.addWidget(QLabel('Revoluciones'), 1, 0)
        layout.addWidget(pbRev, 1, 1)

        layout.addWidget(QLabel('Temperatura'), 2, 0)
        layout.addWidget(pbTemp, 2, 1)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()


    ex.setWindowTitle('UJI MotorSport')
    ex.setWindowIcon(QIcon('icon.ico'))
    ex.resize(1280, 720)
    ex.show()

    sys.exit(app.exec_())

