import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,QLabel)


class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        lb1 = QLabel('Label1')
        lb2 = QLabel('Label2')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Layout Practice')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mywindow()
    sys.exit(app.exec_())
