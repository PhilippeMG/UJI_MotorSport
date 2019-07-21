from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QProgressBar)

import sys


class Dialog(QDialog):

    def slot_method(self):
        print('slot method called.')

    def __init__(self):
        super(Dialog, self).__init__()

        button = QPushButton("Click")
        button.clicked.connect(self.slot_method)

        button1 = QPushButton("Click 1")
        button1.clicked.connect(self.slot_method)

        pbTemp = QProgressBar(self)
        pbTemp.setFixedWidth(500)

        pbTemp.setStyleSheet(
            "QProgressBar::chunk { background-color: #0b8ce8;  margin: 0.5px;}  QProgressBar {text-align: center;}")

        pbTemp.setValue(40)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
        mainLayout.addWidget(button1)
        mainLayout.addWidget(pbTemp)


        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example - pythonspot.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())