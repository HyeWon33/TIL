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
#         self.ui = uic.loadUi("C:/Users/hjw14/Desktop/TIL/SYSTEMPROGRAM/week12.ui", self)
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
        
#         self.rb_adap_methods = {self.radioButton_none: None,
#                                 self.radioButton_otsu: "otsu",
#                                 self.radioButton_adap_mean: "adap_mean",
#                                 self.radioButton_adap_gauss: "adap_gauss"
#                                 }
#         self.rb_adap_group = QButtonGroup()
#         self.sel_adap_method = None

#         self.setup_ui()

#     def setup_ui(self):
#         self.actionOpen.triggered.connect(self.open_file)
#         self.actionSave.triggered.connect(self.save_file)
        
#         self.radioButton_none.setChecked(True) ###
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

#         for rbutton in self.rb_adap_methods:
#             self.rb_adap_group.addButton(rbutton)
#         self.rb_adap_group.buttonPressed.connect(self.update_adap_method)                   

#         self.pushButton_adap_methods.clicked.connect(self.show_adap_methods)
    
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

#         if self.sel_adap_method is None:
#             ret, self.res_img = cv2.threshold(self.src_img,
#                                 self.sel_thresh_value, 255, self.sel_thresh_method)
#         elif self.sel_adap_method == "otsu":
#             ret, self.res_img = cv2.threshold(self.src_img,
#                                 self.sel_thresh_value, 255, self.sel_thresh_method | cv2.THRESH_OTSU)
#             print("otsu selected threshold:", ret)
#         elif self.sel_adap_method == "adap_mean":
#             self.res_img = cv2.adaptiveThreshold(self.src_img, 255,
#                                 cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
#         elif self.sel_adap_method == "adap_gauss":
#             self.res_img = cv2.adaptiveThreshold(self.src_img, 255,
#                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)
#         cv2.imshow("result image", self.res_img)
                


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

#     def update_adap_method(self, rbutton):
#         self.sel_adap_method = self.rb_adap_methods[rbutton]
#         self.update_result()
        

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


#     def show_adap_methods(self):
#         threshold = self.verticalSlider.value()
#         imgs = {"None": self.src_img}
#         ret, imgs["Otsu"] = cv2.threshold(self.src_img, threshold, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#         imgs["Adaptive_Mean"] = cv2.adaptiveThreshold(self.src_img, 255,
#                                     cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
#         imgs["Adaptive_Gauss"] = cv2.adaptiveThreshold(self.src_img, 255,
#                                     cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)

#         for i, (key, value) in enumerate(imgs.items()):
#             plt.subplot(1, 4, i+1)
#             plt.title(key)
#             plt.imshow(value, cmap='gray')
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
















import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"

def blur():
    image = cv2.imread(IMG_PATH + "/yumi-cells.jpg")
    kernel_sizes = [(1, 1), (3, 3), (5, 5), (7, 7), (7, 1), (1, 7)]
    filter_imgs = {}
    blur_imgs = {}
    for ksize in kernel_sizes:
        title = f"ksize : {ksize}"
        kernel = np.ones(ksize)
        kernel /= kernel.size
        filter_imgs[title] = cv2.filter2D(image, -1, kernel)
        blur_imgs[title] = cv2.blur(image, ksize)
    resimg = si.show_imgs(filter_imgs, "cv2.filter2D", 3)
    resimg = si.show_imgs(blur_imgs, "cv2.blur", 3)

def gaussian():
    image = cv2.imread(IMG_PATH + "/yumi-cells.jpg")
    kernel_size = (5, 5)
    blur_imgs = {}
    blur_imgs["original"] = image
    blur_imgs["blur"] = cv2.blur(image, kernel_size)
    blur_imgs["GaussianBlur"] = cv2.GaussianBlur(image, kernel_size, 0)
    result_img = si.show_imgs(blur_imgs, "GaussianBlur", 3, 1000)

def median():
    image = cv2.imread(IMG_PATH + "/ann.jpg")
    median_imgs = dict()
    median_imgs["original"] = image
    median_imgs["median (3)"] = cv2.medianBlur(image, 3)
    median_imgs["median (5)"] = cv2.medianBlur(image, 5)
    result_img = si.show_imgs(median_imgs, "Median Filter", 3)

def bilateral():
    image = cv2.imread(IMG_PATH + "/road.jpg")
    kernel_size = (5, 5)
    blur_imgs = {}
    blur_imgs["original"] = image
    blur_imgs["gaussian"] = cv2.GaussianBlur(image, kernel_size, 0)
    blur_imgs["bilateral (5,50,50)"] = cv2.bilateralFilter(image, 5, 50, 50)
    blur_imgs["bilateral (5,150,150)"] = cv2.bilateralFilter(image, 5, 150, 150)
    result_img = si.show_imgs(blur_imgs, "Bilateral Filter", 2)


if __name__ == "__main__":
    # blur()
    # gaussian()
    # median()
    bilateral()