import cv2 as cv
import numpy as np

img = cv.imread('IMG.jpg')
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = np.array([100, 100, 50])
upper = np.array([255, 255, 255])

mask = cv.inRange(hsv_img, lower, upper)
res = cv.bitwise_and(img, img, mask=mask)

cv.namedWindow('mask', cv.WINDOW_NORMAL)
cv.imshow('mask', mask)

cv.namedWindow('result', cv.WINDOW_NORMAL)
cv.imshow('result', res)
cv.waitKey(0)
cv.destroyAllWindows()

