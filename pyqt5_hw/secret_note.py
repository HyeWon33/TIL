import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


def main():
    app = QApplication(sys.argv)
    editor = MyWindow()
    editor.show()
    app.exec_()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hw3.ui", self)
        self.setup_ui()

    def setup_ui(self):
        QToolTip.setFont(QFont('SansSerif', 10)) 
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.btns()
        self.btn = QPushButton('name', self)
        self.btn.setToolTip('이 버튼을 누르고 노트 주인의 <b>이름</b>을 입력하세요')
        self.btn.move(140, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(200, 300)

        self.setWindowTitle('My Secret Note')
        self.setWindowIcon(QIcon("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hw/note.png")) 
        
        self.show()

    def btns(self):
        self.btn1 = QPushButton('name', self)
        self.btn1.move(20, 30)
        self.btn1.clicked.connect(QCoreApplication.instance().quit)
        self.btn2 = QPushButton('name', self)
        self.btn2.move(260, 30)
        self.btn2.clicked.connect(QCoreApplication.instance().quit)
        self.btn3 = QPushButton('name', self)
        self.btn3.move(380, 30)
        self.btn3.clicked.connect(QCoreApplication.instance().quit)
        
        self.btn4 = QPushButton('name', self)
        self.btn4.move(20, 90)
        self.btn4.clicked.connect(QCoreApplication.instance().quit)
        self.btn5 = QPushButton('name', self)
        self.btn5.move(140, 90)
        self.btn5.clicked.connect(QCoreApplication.instance().quit)
        self.btn6 = QPushButton('name', self)
        self.btn6.move(260, 90)
        self.btn6.clicked.connect(QCoreApplication.instance().quit)
        self.btn7 = QPushButton('name', self)
        self.btn7.move(380, 90)
        self.btn7.clicked.connect(QCoreApplication.instance().quit)

        self.btn8 = QPushButton('name', self)
        self.btn8.move(20, 150)
        self.btn8.clicked.connect(QCoreApplication.instance().quit)
        self.btn9 = QPushButton('name', self)
        self.btn9.move(140, 150)
        self.btn9.clicked.connect(QCoreApplication.instance().quit)
        self.btn10 = QPushButton('name', self)
        self.btn10.move(260, 150)
        self.btn10.clicked.connect(QCoreApplication.instance().quit)
        self.btn11 = QPushButton('name', self)
        self.btn11.move(380, 150)
        self.btn11.clicked.connect(QCoreApplication.instance().quit)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            if text == "정혜원":
                self.le.setText("Hi HyeWon")
                self.second_window()
            else:
                self.le.setText("누구세요")

    def second_window(self):
        window_2 = second_win()


class second_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hw3_2.ui", self)
        self.setup_ui()

    def setup_ui(self):
        self.btn1 = QPushButton("확인", self)
        self.btn1.move(300, 300)
        
        self.quiz()
        self.qc1.clicked.connect(lambda:self.print_cliked(self.qc1))
        self.qc2.clicked.connect(lambda:self.print_cliked(self.qc2))
        self.qc3.clicked.connect(lambda:self.print_cliked(self.qc3))
        self.qc3.clicked.connect(lambda:self.print_cliked(self.qc4))
        self.qc3.clicked.connect(lambda:self.print_cliked(self.qc5))
        self.btn1.clicked.connect(self.check_an)
        self.setWindowTitle('My Secret Note')
        self.setWindowIcon(QIcon("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hw/note.png"))

        self.show()

    def quiz(self):
        self.a = 0
        self.ck1 = "내 생일 1.12"
        self.ck2 = "내 나이 23살"
        self.ck3 = "내 강아지 겨울이"
        self.ck4 = "내 발 230"
        self.ck5 = "내 키 168"
        
        self.qc1 = QCheckBox(self.ck1, self)
        self.qc2 = QCheckBox(self.ck2, self)
        self.qc3 = QCheckBox(self.ck3, self)
        self.qc4 = QCheckBox(self.ck4, self)
        self.qc5 = QCheckBox(self.ck5, self)

        self.qc1.move(10,80)
        self.qc2.move(10,160)
        self.qc3.move(10,240)
        self.qc4.move(10,320)
        self.qc5.move(10,400)

    def print_cliked(self, qc):
        if qc == self.qc1:
            self.a = 100
        
    def check_an(self):
        if self.a == 100:
            print("정답")
            self.qc1.toggle()
            self.third_window()
        else:
            print("땡")
            QCoreApplication.instance().quit()
        self.a = 0

    def third_window(self):
        window_3 = third_win()


class third_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hw3_3.ui", self)
        self.setup_ui()

    def setup_ui(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        self.setWindowTitle('My Secret Note')
        self.setWindowIcon(QIcon("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hw/note.png"))

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        else:
            event.ignore()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(filter="Text files (*.txt)")
        filename = filename[0]
        print("open file:", filename)
        if not filename:
            return
        with open(filename, "r", encoding="utf8") as f:
            text = f.read(10000)
            self.textEdit.setText(text)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(filter="Text files (*.txt)")
        filename = filename[0]
        print("open file:", filename)
        if not filename:
            return
        with open(filename, "w", encoding="utf8") as f:
            f.write(self.textEdit.toPlainText())


if __name__ == "__main__":
    main()
