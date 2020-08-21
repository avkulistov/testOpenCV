import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def with_OCV():
    # читаем изображение как черно-белое
    img = cv.imread('IMG.jpg', cv.IMREAD_GRAYSCALE)

    # выводим изображение
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()
    elif k == ord('s'):
        cv.imwrite('IMG_gray.jpg', img)
        cv.destroyAllWindows()


def with_matplotlib():
    img = cv.imread('IMG.jpg', 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()


def draw_line():
    img = np.zeros((512, 512, 3), np.uint8)
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def canny_edge():
    img = cv.imread('1.jpg', 0)
    edge = cv.Canny(img, 100, 200)

    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', edge)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    # print(cv.__version__)
    # flags = [i for i in dir(cv) if i.startswith('COLOR_')]
    # print(flags)

    canny_edge()
