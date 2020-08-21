import cv2 as cv
import numpy as np

BLUE = [255, 0, 0]

img = cv.imread('IMG.jpg')
replicate = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_CONSTANT, value=BLUE)

cv.namedWindow('ORIGINAL', cv.WINDOW_NORMAL)
cv.imshow('ORIGINAL', img)

cv.namedWindow('REPLICATE', cv.WINDOW_NORMAL)
cv.imshow('REPLICATE', replicate)

cv.namedWindow('REFLECT', cv.WINDOW_NORMAL)
cv.imshow('REFLECT', reflect)

cv.namedWindow('REFLECT_101', cv.WINDOW_NORMAL)
cv.imshow('REFLECT_101', reflect101)

cv.namedWindow('WRAP', cv.WINDOW_NORMAL)
cv.imshow('WRAP', wrap)

cv.namedWindow('CONSTANT', cv.WINDOW_NORMAL)
cv.imshow('CONSTANT', constant)

cv.waitKey(0)
cv.destroyAllWindows()
