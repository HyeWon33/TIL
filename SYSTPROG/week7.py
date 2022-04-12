# 복습
# import numpy as np
# print(np.identity(3)) # identity 정사각형으로만

# print(np.linspace(0, 10, 11)) # 0에서 10까지 11개의 등차수열 
# print(np.arange(0, 10, 1)) # 0에서 10 미만까지 1개씩 늘려간다.


# print(np.random.rand(3, 5))

# data = np.arange(0, 12, 1)
# data = data.reshape(3, 4)
# print(data)
# print(data[0])
# print("-------------------------")
# print(data[0:2])
# print("\n")
# print(data[0:2, 2:])
# print("-------------------------")
# print(data[1, 2:])
# print("-------------------------")
# foo = np.random.randint(0, 10, (3, 4))
# bar = np.random.randint(0, 10, (3, 4))
# print(foo)
# print("-------------------------")
# print(bar)
# print("============================")
# print(foo * bar)
# # print(foo @ bar) # 왜 에러????????????????????????
# print(foo @ bar.T) # bar transpose
# print("-------------------------")
# print(foo[foo>bar])
# print(foo[foo%2==0])



# 2.6

# import numpy as np

# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.rand(5)
# print(foo)
# print("sin : ", np.sin(foo))
# print("cos : ", np.cos(foo))
# print(np.sin(foo) ** 2 + np.cos(foo) ** 2)
# print("exp : ", np.exp(foo))
# print("log : ", np.log(foo))
# print(np.log(np.exp(foo))) # 원래 숫자 그대로 나온다.

# print("sqrt : " , np.sqrt(foo))
# print(np.sqrt(foo) ** 2) # sqrt잘 했나 확인하는거지


# import numpy as np

# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.rand(3, 4)
# print(foo)
# print("mean over all : ", np.mean(foo))
# # 세로 축 평균
# print("mean over rows : ", np.mean(foo, axis=0))
# # 가로 평균
# print("mean over cols : ", np.mean(foo, axis=1))


# import numpy as np

# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.rand(3, 4)
# print(foo)
# print("sum", np.sum(foo, axis=0))
# print("min", np.sum(foo, axis=1)) #min은 axis1 기준 최소값 찾았다.
# print("max", np.max(foo, axis=0))
# print("std", np.std(foo, axis=1))



# #3차원 데이터 만들어서 해보기
# # i did
# # import numpy as np

# # np.set_printoptions(precision=4, suppress=True)

# # foo = np.random.rand(3, 1, 3)
# # print(foo)
# # print("sum", np.sum(foo, axis=0))
# # print("min", np.sum(foo, axis=1))
# # print("max", np.max(foo, axis=0))
# # print("std", np.std(foo, axis=1))

# # p did
# import numpy as np

# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.rand(2, 3, 4)
# print(foo)
# print("axis 0 \n", np.sum(foo, axis=0))
# print("axis 1 \n", np.sum(foo, axis=1))
# print("axis 2 \n", np.sum(foo, axis=2))



# 2.7

# import numpy as np

# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.randint(0, 10, (2, 3))
# bar = np.random.randint(0, 10, (2, 3))
# print("foo \n", foo)
# print("bar \n", bar)

# # stack은 새로운 차원 만들어서 상위 차원에 합치는 것.
# # print("---------------------------")
# # print("stact axis=0 \n", np.stack([foo, bar], axis=0))
# # print("---------------------------")
# # print("stact axis=1 \n", np.stack([foo, bar], axis=1))
# # (2,3) -> (2, 2, 3) 가운데 2가 추가...

# # concat는 있는 차원에 합치는 것.
# print("---------------------------")
# print("stact axis=0 \n", np.stack([foo, bar], axis=0))
# print("concat axis=0 \n", np.concatenate([foo, bar], axis=0)) # 붙이는 모양이다.

# print("---------------------------")
# print("stact axis=1 \n", np.stack([foo, bar], axis=1))
# print("concat axis=1 \n", np.concatenate([foo, bar], axis=1))



# 2.8

# import numpy as np

# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.randint(0, 10, (3, 4))

# print("foo \n", foo)
# # 이렇게 하지 말고
# for i in range(len(foo)):
#     print("row : ", i, foo[i])

# # 이렇게
# for row in foo: # row도 넘파이 배열이라 for 돌 수 있다....
#     print("row: ", row)
#     for elem in row: # 원소 하나씩 꺼내보기
#         print("element : ", elem)


# foo = np.random.randint(0, 10, (3, 4))
# bar = np.random.randint(0, 10, (3, 4))

# print(foo * bar)


# 연습문제 1

# import numpy as np
# np.set_printoptions(precision=4, suppress=True)

# foo = np.random.randint(0, 10, (3, 4))
# bar = np.random.randint(0, 10, (3, 4))
# print("foo \n", foo)
# print("bar \n", bar)

# print("concat axis=0 \n", np.concatenate([foo, bar], axis=0))

#---------------------------------------------------------------

# 연습문제 2

# 내가..
# import numpy as np
# np.set_printoptions(precision=4, suppress=True)

# def find_mean(array, axis=None):
#     a=0
#     array_s=[]
#     if axis==1:
#         print("axis=1 가로줄")
#         array_s = array[0]
#         print(array)
#         for row in array:
#             a+=row
#             m=a/len(array)
#         print(m)

#     else:
#         print("axis=0 세로줄")
#         array = array[0]
#         print(array)
#         for row in array:
#             a+=row
#             m=a/len(array)
#         print(m)

# def main():
#     foo = np.random.randint(0, 10, (2, 2))
#     print("foo \n", foo)

#     find_mean(foo, axis=1)

# if __name__ == "__main__":
#     main()

# 교수님이
# 좋은 문제 아니였다고..

# import numpy as np
# np.set_printoptions(precision=4, suppress=True)


# def find_mean(array, axis=None):
#     result=[]
#     if axis == 0:
#         for i in range(array.shape[1]):
#                 result.append(np.mean(array[:, i]))
#     elif axis == 1:
#         for i in range(array.shape[0]):
#                 result.append(np.mean(array[i]))
#     else:
#         result=0
#         for row in array:
#             for elem in row:
#                 result+=elem
#         result /= array.shape[0] * array.shape[1]
#     return result

# foo = np.random.randint(0, 10, (3, 4))
# print("foo \n", foo)
# print("find_mean \n", find_mean(foo, axis=1))



# PyQt5

# import sys
# from PyQt5.QtWidgets import QApplication, QLabel
# # Widgets이 창

# app = QApplication(sys.argv) 
# label = QLabel("Hello PyQt")
# label.show()
# app.exec_()



# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QCoreApplication


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#         self.count = 0
    
#     def setup_ui(self):
#         self.setWindowTitle("PYQT : basic button event")
#         self.setGeometry(500, 200, 300, 150)
#         print("Window geometry : ", self.geometry())
#         print("window geometry:", self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height())


#         # print("window position, size", self.pos(), self.size())
#         # print push button
        
#         btn_print = QPushButton("Hello", self)
#         btn_print.move(28, 20)
#         btn_print.resize(100, 50)
#         print("btn_print position", btn_print.pos())
#         print("btn_print size", btn_print.size())
#         btn_print.clicked.connect(self.hello_slot)

#         btn_close = QPushButton("닫기", self)
#         btn_close.move(20, 100)
#         btn_close.clicked.connect(QCoreApplication.instance().quit)

#         self.label_print = QLabel("Hello PyQt", self)
#         self.label_print.move(150, 30)

#     def hello_slot(self):
#         self.count += 1
#         self.label_print.setText(f"Hello PyQt {self.count}")


# def main():
#     app = QApplication(sys.argv)
#     my_wnd = MyWindow()
#     my_wnd.show()
#     app.exec_()

# if __name__ == "__main__":
#     main()



# 연습문제

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.count = 0
    
    def setup_ui(self):
        self.setWindowTitle("PYQT : basic button event")
        self.setGeometry(500, 200, 300, 150)
        print("Window geometry : ", self.geometry())
        print("window geometry:", self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height())


        # print("window position, size", self.pos(), self.size())
        # print push button
        
        btn_print = QPushButton("Hello", self)
        btn_print.move(28, 20)
        btn_print.resize(100, 50)
        print("btn_print position", btn_print.pos())
        print("btn_print size", btn_print.size())
        btn_print.clicked.connect(self.hello_slot)

        btn_reset = QPushButton("reset", self)
        btn_reset.move(100, 50)
        btn_reset.clicked.connect(self.reset)




        btn_close = QPushButton("닫기", self)
        btn_close.move(20, 100)
        btn_close.clicked.connect(QCoreApplication.instance().quit)

        self.label_print = QLabel("Hello PyQt", self)
        self.label_print.move(150, 30)

    def hello_slot(self):
        self.count += 1
        self.label_print.setText(f"Hello PyQt {self.count}")

    def reset(self):
        self.count = 0
        self.hello_slot()


def main():
    app = QApplication(sys.argv)
    my_wnd = MyWindow()
    my_wnd.show()
    app.exec_()

if __name__ == "__main__":
    main()