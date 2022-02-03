import cv2 as cv
import numpy as np

RESOLUTION = 800
SHIFT = (RESOLUTION >> 1)
Y, X = np.mgrid[:RESOLUTION, :RESOLUTION] - SHIFT
MY = Y+SHIFT
MX = X+SHIFT


class Mandelbrot:
    rm = 50
    def move_circle(self, event, x, y, flags, param):
        if event == cv.EVENT_MOUSEMOVE:
            img = 100/np.sqrt((X)**2+(Y)**2) + self.rm/np.sqrt((MX-x)**2+(MY-y)**2)
            img = cv.inRange(img, 0.99, 1)
            cv.imshow('image', img)
        if event == cv.EVENT_LBUTTONDOWN:
            self.rm += 10
            self.move_circle(cv.EVENT_MOUSEMOVE, x, y, flags, param)
        if event == cv.EVENT_RBUTTONDOWN:
            self.rm -= 10
            self.move_circle(cv.EVENT_MOUSEMOVE, x, y, flags, param)

mandelbrot = Mandelbrot()

cv.namedWindow('image', cv.WINDOW_GUI_NORMAL | cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('image', mandelbrot.move_circle)
mandelbrot.move_circle(cv.EVENT_MOUSEMOVE, SHIFT, SHIFT, 0, 0)
while True:
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()