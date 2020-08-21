import cv2 as cv
import numpy as np

img = cv.imread('IMG.jpg')
# for i in range(10, 500):
#     for j in range(10, img.shape[1] - 10):
#         # img[i, j] = [0, 0, 0]
#         img.itemset((i, j, 0), 0)
#         img.itemset((i, j, 1), 0)
#         img.itemset((i, j, 2), 0)
img[10:500, 10:img.shape[1] - 10, 2] = 0

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
