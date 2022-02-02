import cv2 as cv
import numpy as np

RESOLUTION = 800
SHIFT = (RESOLUTION >> 1)
Y, X = np.mgrid[:RESOLUTION, :RESOLUTION] - SHIFT
MY = Y+SHIFT
MX = X+SHIFT

def move_circle(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        img = 100/np.sqrt((X)**2+(Y)**2) + 50/np.sqrt((MX-x)**2+(MY-y)**2)
        img = cv.inRange(img, 0.9, 1)
        cv.imshow('image', img)

cv.namedWindow('image')
cv.setMouseCallback('image', move_circle)
move_circle(cv.EVENT_MOUSEMOVE, SHIFT, SHIFT, 0, 0)
while True:
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()