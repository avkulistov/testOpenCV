import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('1.jpg')
kernel = np.ones((8, 8), np.float32)/64
dst = cv.filter2D(img, -1, kernel)
# dst = cv.bilateralFilter(img, 35, 200, 200)
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
