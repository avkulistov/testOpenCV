import cv2 as cv
import numpy as np


def nothing(x):
    pass


cap = cv.VideoCapture(0)
cv.namedWindow('frame')
cv.createTrackbar('Threshold', 'frame', 0, 255, nothing)

while True:
    _, frame = cap.read()

    threshold = cv.getTrackbarPos('Threshold', 'frame')
    blur_frame = cv.GaussianBlur(frame, (5, 5), 0)
    gray_frame = cv.cvtColor(blur_frame, cv.COLOR_BGR2GRAY)
    _, thr_frame = cv.threshold(gray_frame, threshold, 255, cv.THRESH_BINARY)
    # new_frame = cv.bitwise_and(frame, frame, mask=thr_frame)

    cv.imshow('gray_frame', gray_frame)
    # cv.imshow('frame', new_frame)
    cv.imshow('frame', thr_frame)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
