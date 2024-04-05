# coding:utf-8

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 获取灰度图
img = cv2.imread("lenna.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 灰度直方均衡化
dst = cv2.equalizeHist(gray)

hist = cv2.calcHist([dst],[0],None,[256],[0,256])

plt.figure()
plt.hist(dst.ravel(),256)
plt.show()


cv2.imshow("直方图均衡化", np.hstack([gray,dst]))
cv2.waitKey(0)


# 彩色均衡化
# img = cv2.imread("lenna.png",1)
# cv2.imshow("src", img)

# # 分解通道，对每一个通道均衡
# (b,g,r) = cv2.split(img)
# bh = cv2.equalizeHist(b)
# gh = cv2.equalizeHist(g)
# rh = cv2.equalizeHist(r)

# # 合并通道
# result = cv2.merge((bh,gh,rh))
# cv2.imshow("彩色均衡化", result)
# cv2.waitKey(0)