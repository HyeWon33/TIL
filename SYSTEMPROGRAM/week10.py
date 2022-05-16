# import cv2

# image = cv2.imread("C:/Users/hjw14/Desktop/TIL/sample_imgs/superson.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("superson", image)
# key = cv2.waitKey()
# print("key in:", key)
# cv2.destroyAllWindows()



# import cv2
# import os
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "superson.jpg")
# print("filename : ", filename)

# img_color = cv2.imread(filename, cv2.IMREAD_COLOR)
# img_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# img_unchange = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

# cv2.imshow("superson-color", img_color)
# cv2.imshow("superson-gray", img_gray)
# cv2.imshow("superson-unchange", img_unchange)
# key = cv2.waitKey()
# print("key in : ", key, "==", chr(key)) # chr은 숫자를 문자로

# if key == ord('s'): #ord 문자를 숫자로
#     filename = os.path.join(IMG_PATH, "superson-save.jpg")
#     cv2.imwrite(filename, img_color)
# cv2.destroyAllWindows()



# import os
# import cv2

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "endgame.mp4")
# cap = cv2.VideoCapture(filename) # filename 대신 0 넣으면 캠 나온다.
# while 1:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(33) == ord('q'):
#         break

# cap.release()




# import os
# import cv2

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "endgame.mp4")
# cap = cv2.VideoCapture(filename)
# if not cap.isOpened():
#     raise FileNotFoundError()
# print(f'get video property: width={cap.get(cv2.CAP_PROP_FRAME_WIDTH)},'
#     f'height={cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')

# cap.set(cv2.CAP_PROP_POS_MSEC, 20000)

# filename = os.path.join(IMG_PATH, "endgame_rsz.mp4")
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# new_size = (640, 360)
# vout = cv2.VideoWriter(filename, fourcc, 30, new_size)
# if not vout.isOpened():
#     raise FileNotFoundError()

# while 1:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame_rsz = cv2.resize(frame, new_size)
#     cv2.imshow('frame', frame_rsz)
#     if cv2.waitKey(33) == ord('q'):
#         break

#     vout.write(frame_rsz)

# cap.release()
# vout.release()




# import os
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "jjang.jpg")
# image = cv2.imread(filename) 

# print(f"image info : shape={image.shape}, dtyep={image.dtype}, size={image.size}")

# cv2.imshow("jjangzeolmi", image)
# cv2.waitKey()

#image info : shape=(300, 326, 3), dtyep=uint8, size=293400
# 영상의 높이 300, 너비 326, 채널이 BGR로 3채널 이라는 뜻
# rgb값은 0에서 255사이 정수 값 갖을 수 있다.
# 300*326*3 = size
# opencv에서 numpy형식으로 이미지데이터를 저장하고 조작한다.



# import os
# from turtle import bgcolor
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "jjang.jpg")
# image = cv2.imread(filename) 

# print(f"image info : shape={image.shape}, dtyep={image.dtype}, size={image.size}")

# cv2.imshow("jjangzeolmi", image)
# cv2.waitKey()

# channels = {"blue", "green", "red"}
# bgr_means = {}

# # for chn, color in enumerate(channels):
# #     color_sum = 0
# #     for v in range(image.shape[0]): #shape[0]은 이미지의 높이. 행의 인덱스
# #         for u in range(image.shape[1]):
# #             color_sum += image[v, u, chn] #세로, 가로, 채널인덱스
# #     bgr_means[color] = color_sum / image[:, :, chn].size
# # print("BGR means : ", bgr_means)

# # ↕ 위 아래 같다...

# for chn, color in enumerate(channels):
#     bgr_means[color] = np.mean(image[:,:,chn])
# print("BGR means : ", bgr_means)






# import os
# from turtle import bgcolor
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "jjang.jpg")
# image = cv2.imread(filename) 
# print(f"image info : shape={image.shape}, dtyep={image.dtype}, size={image.size}")

# image[:10] = 120 # 위에 회색 줄
# image[-10:] = 0 # 아래에 검은 줄
# # image[:, :10] = (255,0,0) # 왼쪽 파란 줄 
# image[:, :10, 0] = 255
# # image[:, :10, 1:] = 0 #(0,0) ????
# image[:, -10:, :] = (0, 0, 255)

# cv2.imshow("jjangzeolmi", image)
# cv2.waitKey()

# 높이 너비

# 연습문제 네모그리기

# import os
# from turtle import bgcolor
# import cv2
# import numpy as np

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "jjang.jpg")
# image = cv2.imread(filename) 
# print(f"image info : shape={image.shape}, dtyep={image.dtype}, size={image.size}")

# image[100:200, 100] = (0, 0, 255) 
# image[100, 100:200] = (0, 0, 255) 
# image[100:200, 200] = (0, 0, 255)
# image[200, 100:200] = (0, 0, 255)  
# cv2.imshow("jjangzeolmi", image)
# cv2.waitKey()




# import os
# import cv2

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "makrae.jpg")
# srcimg = cv2.imread(filename) 
# shapeimg = srcimg.copy()

# #인덱스 yx 입력인자 xy 리사이즈 너비 높이
# cv2.line(shapeimg, pt1=(50,110), pt2=(105, 110), color=(255, 0, 0), thickness=2)
# cv2.circle(shapeimg, center=(33, 150), radius=20, color=(0, 0, 255), thickness=2)
# cv2.rectangle(shapeimg, pt1=(160, 20), pt2=(340, 240), color=(0, 255, 0), thickness=1)
# cv2.putText(shapeimg, text="Korea Grandma", org=(360, 100), 
#     fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(50, 50, 50), thickness=2)

# cv2.imshow("original", srcimg)
# cv2.imshow("draw shape", shapeimg)
# cv2.waitKey()




# #할머니 눈에 동그라미
# import os
# import cv2

# IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
# filename = os.path.join(IMG_PATH, "makrae.jpg")
# srcimg = cv2.imread(filename) 
# shapeimg = srcimg.copy()

# #인덱스 yx 입력인자 xy 리사이즈 너비 높이
# cv2.line(shapeimg, pt1=(50,110), pt2=(105, 110), color=(255, 0, 0), thickness=2)
# cv2.circle(shapeimg, center=(230, 140), radius=20, color=(0, 0, 255), thickness=2)
# cv2.rectangle(shapeimg, pt1=(160, 20), pt2=(340, 240), color=(0, 255, 0), thickness=1)
# cv2.putText(shapeimg, text="Korea Grandma", org=(360, 100), 
#     fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(50, 50, 50), thickness=2)

# cv2.imshow("original", srcimg)
# cv2.imshow("draw shape", shapeimg)
# cv2.waitKey()





# import os
# import cv2

# class MouseEventHandler:
#     def __init__(self, title, image):
#         self.title = title
#         self.image = image.copy()
#         self.pt1 = (0, 0)

#     def on_mouse_event(self, event, x, y, flags, param):
#         if event == cv2.EVENT_LBUTTONDOWN:
#             self.pt1 = (x, y)
#             print("set pt1", self.pt1)
#         elif event == cv2.EVENT_MOUSEMOVE:
#             pass
#         elif event == cv2.EVENT_LBUTTONUP:
#             if self.pt1 == (x, y):
#                 return
#             print("set pt2", (x, y))
#             cv2.line(self.image, pt1=self.pt1, pt2=(x, y), color=(255, 0, 0))
#             cv2.imshow(self.title, self.image)

# def draw_line():
#     IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
#     filename = os.path.join(IMG_PATH, "makrae.jpg")
#     srcimg = cv2.imread(filename)
#     window_name = "line_drawing"
#     cv2.imshow(window_name, srcimg)

#     mouse_hndl = MouseEventHandler(window_name, srcimg)
#     cv2.setMouseCallback(window_name, mouse_hndl.on_mouse_event)
#     cv2.waitKey()


# if __name__ == "__main__":
#     draw_line()




# def foo():
#     print("foo")
#     def qoo():
#         print("qoqoqo")
#     return qoo

# class bar:
#     def bar_func(self):
#         print("bar")

# def spam(f1, f2):
#     f1()
#     f2()

# # eggs = bar()
# # goo = foo
# # # spam(foo, eggs.bar_func)
# # spam(goo, eggs.bar_func)

# bar = foo()
# bar()





# 연습문제

# import os
# import cv2

# class MouseEventHandler:
#     def __init__(self, title, image):
#         self.title = title
#         self.image = image.copy()
#         self.pt1 = (0, 0)

#     def on_mouse_event(self, event, x, y, flags, param):
#         if event == cv2.EVENT_MOUSEMOVE:

#             # # 기본
#             # self.image[y, x] = (0, 0, 255)
#             # cv2.imshow(self.title, self.image)

#             # 두꺼운 점
#             self.image[y-1:y+1, x-1:x+1] = (0, 0, 255) #두 칸 지정
#             cv2.imshow(self.title, self.image)

#             # if self.pt1 == (x, y):
#             #     return
#             # print("set pt2", (x, y))
#             # cv2.polylines(self.image, pt1=self.pt1, pt2=(x, y), color=(255, 0, 0))
#             # cv2.imshow(self.title, self.image)


# def draw_line():
#     IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
#     filename = os.path.join(IMG_PATH, "makrae.jpg")
#     srcimg = cv2.imread(filename)
#     window_name = "line_drawing"
#     cv2.imshow(window_name, srcimg)

#     mouse_hndl = MouseEventHandler(window_name, srcimg)
#     cv2.setMouseCallback(window_name, mouse_hndl.on_mouse_event)
#     cv2.waitKey()


# if __name__ == "__main__":
#     draw_line()







import os
import cv2
import numpy as np

IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"
filename = os.path.join(IMG_PATH, "spiderman.jpg")
bgrimg = cv2.imread(filename)   

grayimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2GRAY)

#바이너리 만드는 것ㄱ은 없어서 그레이에서 복사해서 
binaryimg = grayimg.copy()
binaryimg[grayimg < 120] = 0
binaryimg[grayimg >= 120] = 255

grayimg = cv2.cvtColor(grayimg, cv2.COLOR_GRAY2BGR)
binaryimg = cv2.cvtColor(binaryimg, cv2.COLOR_GRAY2BGR)

concatimg = np.concatenate([binaryimg, grayimg, bgrimg], axis=1)
cv2.imshow("binary gray BGR", concatimg)
# cv2.waitKey()

# 채널을 다시 나누고 가로로 합치기 300X900이 된다.
channels = np.concatenate([bgrimg[:,:,0], bgrimg[:,:,1], bgrimg[:,:,2]], axis=1)
cv2.imshow("BGR channels", channels)
cv2.waitKey()