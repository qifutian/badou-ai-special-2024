#coding=utf-8

import cv2 as cv
img = cv.imread("lenna.png")
cv.imshow("hello,python opencv",img)
cv.waitKey(0)
cv.destroyAllWindows()