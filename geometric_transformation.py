import cv2 as cv
import numpy as np


def resize():
    img = cv.imread('IMG.jpg')
    res = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
    cv.imshow('resize', img)
    cv.waitKey(0)


def translation():
    img = cv.imread('IMG.jpg', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.namedWindow('img', cv.WINDOW_NORMAL)
    cv.imshow('img', dst)
    cv.waitKey(0)


def rotation():
    img = cv.imread('IMG.jpg', 0)
    rows, cols = img.shape
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 25, 1)
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.namedWindow('img', cv.WINDOW_NORMAL)
    cv.imshow('img', dst)
    cv.waitKey(0)


# resize()
rotation()
cv.destroyAllWindows()
