import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 绘制界面的方法，直接初始化中完成。

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('MyWindow')

        self.show()


if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    ex = MyWindow()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
