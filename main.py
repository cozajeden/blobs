import cv2 as cv
import numpy as np

RESOLUTION = 800
SHIFT = (RESOLUTION >> 1)
Y, X = np.mgrid[:RESOLUTION, :RESOLUTION] - SHIFT
MY = Y-SHIFT
MX = X+SHIFT

def move_circle(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        img = 100/np.sqrt((X)**2+(Y)**2) + 50/np.sqrt((MX-x)**2+(MY+y)**2)
        _, img = cv.threshold(img[::-1,:], 1, 255, cv.THRESH_BINARY)
        img = cv.GaussianBlur(img, (3,3), 0, 0)
        imgx = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=3, scale=1)
        imgy = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=3, scale=1)
        imgxy = cv.Sobel(img, cv.CV_16S, 1, 1, ksize=3, scale=1)
        img = cv.addWeighted(imgx, 0.5, imgy, 0.5, 0)
        img = cv.addWeighted(imgxy, 0.33, img, 0.66, 0)
        img = cv.inRange(img, 0, 0)
        img = cv.normalize(img, None, 0, 255, cv.NORM_MINMAX)
        cv.imshow('image', img)

cv.namedWindow('image')
cv.setMouseCallback('image', move_circle)
move_circle(cv.EVENT_MOUSEMOVE, SHIFT, SHIFT, 0, 0)
while True:
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()