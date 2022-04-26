import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QCoreApplication #
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #UI 불러오기
        self.ui = uic.loadUi("hellopyqt.ui", self)

        self.btn_print.clicked.connect(self.hello_slot) #
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        self.count = 0
        print("window geometry : ", self.geometry())
        print("btn_print position : ", self.btn_print.pose())
        print("btn_print size : ", self.btn_print.size())

        def hello_slot(slef):
            self.count = self.count+1
            self.label_print.setText(f"Hello PyQt {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

