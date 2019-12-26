import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 绘制界面的方法，直接初始化中完成。

    def initUI(self):
        # 设置窗口大小
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('MyWindow')
        # 设置字体使用静态方法
        QToolTip.setFont(QFont('Open Sans', 10))
        self.setToolTip('This is a <b>QWidget</b> widget!')

        # 创建按钮并且设置tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a button!')
        btn.resize(btn.sizeHint())
        btn.move(50,10) # 设置按钮位置

        # 创建退出按钮
        btnquit = QPushButton('Quit', self)
        btnquit.clicked.connect(QCoreApplication.instance().quit)
        btnquit.resize(btnquit.sizeHint())
        btnquit.move(50,40)

        # 创建label
        lbl1 = QLabel('This is a label',self)
        lbl1.move(50,60)

        self.show()


if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    window = MyWindow()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
