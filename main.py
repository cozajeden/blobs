import cv2 as cv
import numpy as np

y, x = np.mgrid[:512, :512] - 256
steps = np.linspace(0, np.pi, 200)
xx = (np.sin(steps)+ np.sin(5*steps)+np.cos(3*steps))*150
yy = (np.cos(steps)+ np.cos(11*steps)+np.sin(5*steps))*150
for x0, y0 in zip(xx, yy):
    img = 200/np.sqrt((x)**2+(y)**2) + 100/np.sqrt((x-x0)**2+(y+y0)**2)
    _, img = cv.threshold(
        img[::-1,:],
        2,
        255,
        cv.THRESH_BINARY
    )
    cv.imshow('img', img)
    cv.waitKey(40)
cv.destroyAllWindows()