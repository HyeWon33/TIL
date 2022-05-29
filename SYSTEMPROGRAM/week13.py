import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "C:/Users/hjw14/Desktop/TIL/sample_imgs"

def sobel():
    image = cv2.imread(IMG_PATH + '/yumi-cells.jpg', cv2.IMREAD_GRAYSCALE)
    sobel_imgs = {"original" : image}
    sobel_imgs["Sobel dx"] = cv2.Sobel(image, ddepth=-1, dx=1, dy=0, ksize=3)
    sobel_imgs["Sobel dy"] = cv2.Sobel(image, ddepth=-1, dx=0, dy=1, ksize=3)
    sobel_imgs["Sobel dx+dy"] = cv2.add(sobel_imgs["Sobel dx"], sobel_imgs["Sobel dy"])
    sobel_imgs["Scharr dx"] = cv2.Scharr(image, ddepth=-1, dx=1, dy=0)
    sobel_imgs["Scharr dy"] = cv2.Scharr(image, ddepth=-1, dx=0, dy=1)
    result_img = si.show_imgs(sobel_imgs, "Sobel & Scharr", 3)

def laplacian():
    image = cv2.imread(IMG_PATH + "/yumi-cells.jpg", cv2.IMREAD_GRAYSCALE)
    lapla_imgs = {"original" : image}
    sobel_dx = cv2.Sobel(image, ddepth=-1, dx=1, dy=0, ksize=3)
    sobel_dy = cv2.Sobel(image, ddepth=-1, dx=0, dy=1, ksize=3)
    lapla_imgs["Sobel dx+dy"] = cv2.add(sobel_dx, sobel_dy) #뭐 넘어갈까봐 add...
    lapla_imgs["Laplacian"] = cv2.Laplacian(image, -1)
    result_img = si.show_imgs(lapla_imgs, "Laplacian", 3)

def canny():
    image = cv2.imread(IMG_PATH + "/arya.jpg", cv2.IMREAD_GRAYSCALE)
    canny_imgs = {"original" : image}
    canny_imgs["Laplacian"] = cv2.Laplacian(image, -1, scale=2)
    canny_imgs["Canny (100, 200)"] = cv2.Canny(image, 100, 200)
    canny_imgs["Canny (150, 255)"] = cv2.Canny(image, 150, 255)
    result_img = si.show_imgs(canny_imgs, "Canny", 2)

def erode_and_dilate():
    srcimg = cv2.imread(IMG_PATH + "/marvel.jpg", cv2.IMREAD_GRAYSCALE)
    srcimg = salt_and_pepper_noise(srcimg)

    images = {"original": srcimg}
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    images["erode"] = cv2.erode(srcimg, kernel)
    images["dilae"] = cv2.dilate(srcimg, kernel)
    result_img = si.show_imgs(images, "Erode and Dilate", 1)

def salt_and_pepper_noise(image):
    towhite = np.unravel_index(np.random.randint(0, image.size, 100), image.shape)
    toblack = np.unravel_index(np.random.randint(0, image.size, 100), image.shape)
    image[towhite] = 255
    image[toblack] = 0
    return image

def morphologies():
    srcimg = cv2.imread(IMG_PATH + "/marvel.jpg", cv2.IMREAD_GRAYSCALE)
    srcimg = salt_and_pepper_noise(srcimg)

    images = {"original" : srcimg}
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    images["opening"] = cv2.morphologyEx(srcimg, cv2.MORPH_OPEN, kernel)
    images["closing"] = cv2.morphologyEx(srcimg, cv2.MORPH_CLOSE, kernel)
    images["graient"] = cv2.morphologyEx(srcimg, cv2.MORPH_GRADIENT, kernel)
    images["tophat"] = cv2.morphologyEx(srcimg, cv2.MORPH_TOPHAT, kernel)
    images["blackhat"] = cv2.morphologyEx(srcimg, cv2.MORPH_BLACKHAT, kernel)
    result_img = si.show_imgs(images, "Morphology Ops", 2)


def hough_lines():
    img_names = [IMG_PATH + f"/bookshelf{i+1}.jpg" for i in range(3)]
    images = {}
    for i, name in enumerate(img_names):
        srcimg = cv2.imread(name, cv2.IMREAD_COLOR)
        images[f"srcimg{i+1}"] = srcimg

        grayimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)
        blurimg = cv2.GaussianBlur(grayimg, (3, 3), 0)
        cannyimg = cv2.Canny(blurimg, 100, 200)
        images[f"canny{i+1}"] = cannyimg


        lines = cv2.HoughLinesP(cannyimg, 1, np.pi/180, 50, None, 50, 10)
        print("lines", lines)
        result = images[f"srcimg{i+1}"].copy
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(result, (x1,y1), (x2,y2), (0,0,255), 1)
        images[f"houghline{i+1}"] = result





    result_img = si.show_imgs(images, "hough lines", 3, 1200)





if __name__ == "__main__":
    # sobel()
    # laplacian()
    # canny()
    # erode_and_dilate()
    # morphologies()
    hough_lines()