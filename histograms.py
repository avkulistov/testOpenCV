import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def calc_hist():
    img = cv.imread('IMG.jpg', 0)
    hist = cv.calcHist([img], [0], None, [256], [0, 256])

    hist2, bins = np.histogram(img.ravel(), 256, [0, 256])

    hist3 = np.bincount(img.ravel(), minlength=256)

    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def hist_bgr():
    img = cv.imread('IMG.jpg')
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


def equalize():
    img = cv.imread('wiki.jpg', 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    # plt.show()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    img2 = cdf[img]
    cv.imshow('image1', img)
    cv.imshow('image', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()


def equalize_cv():
    img = cv.imread('wiki.jpg', 0)
    equ = cv.equalizeHist(img)
    cv.imshow('equ', equ)
    cv.waitKey(0)
    res = np.hstack((img, equ))
    cv.imwrite('res.jpg', res)
    cv.destroyAllWindows()

equalize_cv()
