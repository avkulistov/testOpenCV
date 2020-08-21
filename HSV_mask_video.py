import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # red color
    low_red = np.array([161, 120, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv.inRange(hsv_frame, low_red, high_red)
    red = cv.bitwise_and(frame, frame, mask=red_mask)

    # blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv.inRange(hsv_frame, low_blue, high_blue)
    blue = cv.bitwise_and(frame, frame, mask=blue_mask)

    # green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv.inRange(hsv_frame, low_green, high_green)
    green = cv.bitwise_and(frame, frame, mask=green_mask)

    cv.imshow('frame', frame)
    cv.imshow('red', red)
    cv.imshow('blue', blue)
    cv.imshow('green', green)
    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()
