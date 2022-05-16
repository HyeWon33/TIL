# 22년 04월 26일 화요일

## 복습

## 참고문서 찾기

- https://doc.qt.io/qt-5.15/classes.html
- 대다수의 함수를 부모클래스인 `QWidget`에서 물려받았기 때문에 `QWidget` 클래스 문서로 들어가야 `setGeometry()` 함수에 대한 설명을 볼 수 있다. 하지만 굳이 부모클래스를 찾아갈 필요없이 첫 화면에 보이는 `List of all members, including inherited members` 라는 링크로 들어가면 상속받은 모든 함수를 볼 수 있으므로 여기서 해당 함수를 검색하면 찾을 수 있다.



## Simple QtDesigner Example





```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QCoreApplication #
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #UI 불러오기
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hellopyqt.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

```

- 나는 전체 경로를 써줘야 실행되었다. 
- 그리고 \ -> /로 쓰기!

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 불러오기
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/hellopyqt.ui", self)
        # signal - slot 연결
        self.btn_print.clicked.connect( self.hello_slot )
        self.btn_close.clicked.connect( QCoreApplication.instance().quit )
        self.count = 0
        print("window geometry:", self.geometry())
        print("btn_print position:", self.btn_print.pos())
        print("btn_print size:", self.btn_print.size())

    def hello_slot(self):
        self.count = self.count + 1
        self.label_print.setText(f"Hello PyQt {self.count}")

def main():
    app = QApplication(sys.argv)
    my_wnd = MyWindow()
    # my_wnd attribute 목록 출력하기
    print(dir(my_wnd))
    print([attr for attr in dir(my_wnd) if attr.startswith("btn") or attr.startswith("label")])
    # => ['btn_close', 'btn_print', 'label_print']
    my_wnd.show()
    app.exec_()

if __name__ == "__main__":
    main()
```









# Implement GUI Text Editor

```python
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/text_editor.ui", self)

def main():
    app = QApplication(sys.argv)
    editor = MyWindow()
    editor.show()
    app.exec_()

if __name__ == "__main__":
    main()
```

