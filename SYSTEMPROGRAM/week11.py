# import os
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "spiderman.jpg")
# bgrimg = cv2.imread(filename)   

# hsvimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2HSV)

# channels = np.concatenate([hsvimg[:,:,0], hsvimg[:,:,1], hsvimg[:,:,2]], axis=1)
# print("image shapes : ", hsvimg.shape, hsvimg[:,:,0].shape, channels.shape)

# cv2.imshow("HSV channels", channels)
# cv2.waitKey()



#HSV는 밝기와 색상이 분리되어있다. 그래서 밝기가 다르더라도 같은 색상 추출하는데 더 유리하다.



# import os
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "spiderman.jpg")
# bgrimg = cv2.imread(filename)   

# hsvimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2HSV)

# #이미지 변환
# hueimg = hsvimg[:, :, 0]
# valueimg = hsvimg[:, :, 2]
# faceimg = np.zeros(bgrimg.shape, dtype=np.uint8)

# faceimg[hueimg<13, :] = bgrimg[hueimg<13, :]

# # cv2.imshow("face image", faceimg)
# # cv2.waitKey()

# bodyimg = np.zeros(bgrimg.shape, dtype=np.uint8)
# bodyimg[hueimg>170, :] = bgrimg[hueimg>170, :]




# 간단한 numpy 연습

# import numpy as np

# foo = np.zeros((3, 4), dtype=int)
# bar = np.random.randint(0, 10, (3, 4))
# goo = np.random.randint(0, 10, (3, 4))
# print(foo)
# print(bar)
# print(goo)
# print("=======================================")
# #foo에다가 goo가 6 이상인 영역에 bar의 값들을 가져오고싶다.
# foo[goo > 6] = bar[goo > 6]
# #goo에서 6보다 큰 값 자리에 bar의 값들이 들어갔다.
# print(foo)



#다시
# import os
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "spiderman.jpg")
# bgrimg = cv2.imread(filename)   

# hsvimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2HSV)

# #이미지 변환
# hueimg = hsvimg[:, :, 0]
# valueimg = hsvimg[:, :, 2]
# faceimg = np.zeros(bgrimg.shape, dtype=np.uint8)

# faceimg[hueimg<13, :] = bgrimg[hueimg<13, :]

# # cv2.imshow("face image", faceimg)
# # cv2.waitKey()

# bodyimg = np.zeros(bgrimg.shape, dtype=np.uint8)
# bodyimg[hueimg>170] = bgrimg[hueimg>170] #빨
# bodyimg[(hueimg > 100) & (hueimg < 130)] = bgrimg[(hueimg > 100) & (hueimg < 130)] #파
# bodyimg[valueimg > 220] = 0 #value높아서 파이면서 value 높은 곳은 지운다.

# cv2.imshow("body image", bodyimg)
# cv2.waitKey()




#YUV는 밝기 강조


# import os
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "spiderman.jpg")
# bgrimg = cv2.imread(filename)   

# yuvimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2YUV)
# # channels = np.concatenate([yuvimg[:,:,0], yuvimg[:,:,1], yuvimg[:,:,2]], axis=1)
# channels = np.concatenate([yuvimg[:, :, i] for i in range(3)], axis=1)
# cv2.imshow("YUV channels", channels)
# cv2.waitKey()




# import os
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "sungmo.jpg")
# image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# ret, binary = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)

# showimg = np.concatenate([image, binary], axis=1)
# cv2.imshow("thresolding", showimg)
# cv2.waitKey()




# import sys
# import cv2
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# import matplotlib.pylab as plt

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/week10.ui", self)
#         self.src_img = None
#         self.res_img = None
#         self.setup_ui()

#     def setup_ui(self):
#         self.actionOpen.triggered.connect(self.open_file)
#         self.actionSave.triggered.connect(self.save_file)

#     def save_file(self):
#         filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)", directory="C:/Users/hjw14/Desktop/TIL/sample_imgs")
#         filename = filename[0]
#         print("save file : ", filename)
#         if not filename or self.res_img in None:
#             return
#         cv2.imwrite(filename, self.res_img)


#     def open_file(self):
#         filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)")
#         filename = filename[0]

#         print("open file : ", filename)
#         if not filename:
#             return
#         self.src_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#         cv2.imshow("original", self.src_img)
#         cv2.waitKey(1)
        



# def main():
#     app = QApplication(sys.argv)
#     editor = MyWindow()
#     editor.show()
#     app.exec_()

# if __name__ == "__main__":
#     main()








# import sys
# import cv2
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# from pandas import value_counts
# import matplotlib.pylab as plt

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/week10.ui", self)
#         self.src_img = None
#         self.res_img = None

#         self.rb_thresh_methods = {self.radioButton_binary: cv2.THRESH_BINARY,
#                                   self.radioButton_binary_inv: cv2.THRESH_BINARY_INV,
#                                   self.radioButton_trunc: cv2.THRESH_TRUNC,
#                                   self.radioButton_tozero: cv2.THRESH_TOZERO,
#                                   self.radioButton_tozero_inv: cv2.THRESH_TOZERO_INV,
#                                   }

#         self.rb_method_group = QButtonGroup()
#         self.sel_thresh_method = cv2.THRESH_BINARY
#         self.sel_thresh_value = 100

#         self.setup_ui()

#     def setup_ui(self):
#         self.actionOpen.triggered.connect(self.open_file)
#         self.actionSave.triggered.connect(self.save_file)

#         # slider settings
#         self.radioButton_binary.setChecked(True) #미리 기본값으로 선택
#         self.verticalSlider.setMaximum(255)
#         self.verticalSlider.setMinimum(0)
#         self.verticalSlider.setValue(self.sel_thresh_value)

#         # threshold method
#         for rbutton in self.rb_thresh_methods:
#             self.rb_method_group.addButton(rbutton)
#         self.rb_method_group.buttonPressed.connect(self.update_thresh_method)
#         # threshold value
#         self.verticalSlider.valueChanged.connect(self.update_thresh_value)
    
#     def update_thresh_method(self, rbutton):
#         self.sel_thresh_method = self.rb_thresh_methods[rbutton]
#         self.update_result()

#     def update_thresh_value(self, value):
#         self.sel_thresh_value = value
#         text = f"Threshold : {self.sel_thresh_value}"
#         self.label_threshold.setText(text)

#         self.update_result()


#     def update_result(self):
#         ret, self.res_img = cv2.threshold(self.src_img, self.sel_thresh_value, 255, self.sel_thresh_method)
#         cv2.imshow("result image", self.res_img)
#         cv2.waitKey(1)


#     def save_file(self):
#         filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)", directory="C:/Users/hjw14/Desktop/TIL/sample_imgs")
#         filename = filename[0]
#         print("save file : ", filename)
#         if not filename or self.res_img in None:
#             return
#         cv2.imwrite(filename, self.res_img)


#     def open_file(self):
#         filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)")
#         filename = filename[0]

#         print("open file : ", filename)
#         if not filename:
#             return
#         self.src_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#         cv2.imshow("original", self.src_img)
#         cv2.waitKey(1)
        



# def main():
#     app = QApplication(sys.argv)
#     editor = MyWindow()
#     editor.show()
#     app.exec_()

# if __name__ == "__main__":
#     main()









# import sys
# import cv2
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# from cv2 import threshold
# from pandas import value_counts
# import matplotlib.pylab as plt

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/week10.ui", self)
#         self.src_img = None
#         self.res_img = None

#         self.rb_thresh_methods = {self.radioButton_binary: cv2.THRESH_BINARY,
#                                   self.radioButton_binary_inv: cv2.THRESH_BINARY_INV,
#                                   self.radioButton_trunc: cv2.THRESH_TRUNC,
#                                   self.radioButton_tozero: cv2.THRESH_TOZERO,
#                                   self.radioButton_tozero_inv: cv2.THRESH_TOZERO_INV,
#                                   }

#         self.rb_method_group = QButtonGroup()
#         self.sel_thresh_method = cv2.THRESH_BINARY
#         self.sel_thresh_value = 100

#         self.setup_ui()

#     def setup_ui(self):
#         self.actionOpen.triggered.connect(self.open_file)
#         self.actionSave.triggered.connect(self.save_file)

#         # slider settings
#         self.radioButton_binary.setChecked(True) #미리 기본값으로 선택
#         self.verticalSlider.setMaximum(255)
#         self.verticalSlider.setMinimum(0)
#         self.verticalSlider.setValue(self.sel_thresh_value)

#         # threshold method
#         for rbutton in self.rb_thresh_methods:
#             self.rb_method_group.addButton(rbutton)
#         self.rb_method_group.buttonPressed.connect(self.update_thresh_method)
#         # threshold value
#         self.verticalSlider.valueChanged.connect(self.update_thresh_value)

#         self.pushButton_thresh_types.clicked.connect(self.show_all_types)

    
#     def update_thresh_method(self, rbutton):
#         self.sel_thresh_method = self.rb_thresh_methods[rbutton]
#         self.update_result()

#     def update_thresh_value(self, value):
#         self.sel_thresh_value = value
#         text = f"Threshold : {self.sel_thresh_value}"
#         self.label_threshold.setText(text)

#         self.update_result()


#     def update_result(self):
#         ret, self.res_img = cv2.threshold(self.src_img, self.sel_thresh_value, 255, self.sel_thresh_method)
#         cv2.imshow("result image", self.res_img)
#         cv2.waitKey(1)


#     def save_file(self):
#         filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)", directory="C:/Users/hjw14/Desktop/TIL/sample_imgs")
#         filename = filename[0]
#         print("save file : ", filename)
#         if not filename or self.res_img in None:
#             return
#         cv2.imwrite(filename, self.res_img)


#     def open_file(self):
#         filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)")
#         filename = filename[0]

#         print("open file : ", filename)
#         if not filename:
#             return
#         self.src_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#         cv2.imshow("original", self.src_img)
#         cv2.waitKey(1)
        

#     def show_all_types(self):
#         threshold = self.verticalSlider.value()
#         imgs = {"ORIGINAL": self.src_img}
#         for rbutton, thresh_method in self.rb_thresh_methods.items():
#             ret, res_binary = cv2.threshold(self.src_img, threshold, 255, thresh_method)
#             imgs[rbutton.text()] = res_binary
#         imgs['TRUNC'][0, 0] = 255

#         for i, (title, image) in enumerate(imgs.items()):
#             plt.subplot(2, 3, i+1)
#             plt.title(title)
#             plt.imshow(image, cmap='gray')
#             plt.xticks([])
#             plt.yticks([])
#         plt.tight_layout()
#         plt.show()



# def main():
#     app = QApplication(sys.argv)
#     editor = MyWindow()
#     editor.show()
#     app.exec_()

# if __name__ == "__main__":
#     main()







#Threshold를 할 때 가장 중요한 것은 경계 값(thresh)을 얼마로 정하느냐


import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5 import uic
from cv2 import threshold
from pandas import value_counts
import matplotlib.pylab as plt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/week10.ui", self)
        self.src_img = None
        self.res_img = None

        self.rb_thresh_methods = {self.radioButton_binary: cv2.THRESH_BINARY,
                                  self.radioButton_binary_inv: cv2.THRESH_BINARY_INV,
                                  self.radioButton_trunc: cv2.THRESH_TRUNC,
                                  self.radioButton_tozero: cv2.THRESH_TOZERO,
                                  self.radioButton_tozero_inv: cv2.THRESH_TOZERO_INV,
                                  }

        self.rb_method_group = QButtonGroup()
        self.sel_thresh_method = cv2.THRESH_BINARY
        self.sel_thresh_value = 100

        self.setup_ui()

    def setup_ui(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        # slider settings
        self.radioButton_binary.setChecked(True) #미리 기본값으로 선택
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setValue(self.sel_thresh_value)

        # threshold method
        for rbutton in self.rb_thresh_methods:
            self.rb_method_group.addButton(rbutton)
        self.rb_method_group.buttonPressed.connect(self.update_thresh_method)
        # threshold value
        self.verticalSlider.valueChanged.connect(self.update_thresh_value)

        self.pushButton_thresh_types.clicked.connect(self.show_all_types)

    
    def update_thresh_method(self, rbutton):
        self.sel_thresh_method = self.rb_thresh_methods[rbutton]
        self.update_result()

    def update_thresh_value(self, value):
        self.sel_thresh_value = value
        text = f"Threshold : {self.sel_thresh_value}"
        self.label_threshold.setText(text)

        self.update_result()


    def update_result(self):
        ret, self.res_img = cv2.threshold(self.src_img, self.sel_thresh_value, 255, self.sel_thresh_method)
        cv2.imshow("result image", self.res_img)
        cv2.waitKey(1)


    def save_file(self):
        filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)", directory="C:/Users/hjw14/Desktop/TIL/sample_imgs")
        filename = filename[0]
        print("save file : ", filename)
        if not filename or self.res_img in None:
            return
        cv2.imwrite(filename, self.res_img)


    def open_file(self):
        filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)")
        filename = filename[0]

        print("open file : ", filename)
        if not filename:
            return
        self.src_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("original", self.src_img)
        cv2.waitKey(1)
        

    def show_all_types(self):
        threshold = self.verticalSlider.value()
        imgs = {"ORIGINAL": self.src_img}
        for rbutton, thresh_method in self.rb_thresh_methods.items():
            ret, res_binary = cv2.threshold(self.src_img, threshold, 255, thresh_method)
            imgs[rbutton.text()] = res_binary
        imgs['TRUNC'][0, 0] = 255

        for i, (title, image) in enumerate(imgs.items()):
            plt.subplot(2, 3, i+1)
            plt.title(title)
            plt.imshow(image, cmap='gray')
            plt.xticks([])
            plt.yticks([])
        plt.tight_layout()
        plt.show()



def main():
    app = QApplication(sys.argv)
    editor = MyWindow()
    editor.show()
    app.exec_()

if __name__ == "__main__":
    main()