# 随机生成正态高斯 分步随机数，means，sigma两参数

import numpy as np
import cv2
from numpy import shape
import random

def GaussianNoise(src, means, sigma,percetage):
    NoiseImg = src
    NoiseNum = int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        # 每次去的一个随机点
        # 一张图片用行列表示，randX随机行，ranY随机列
        # random.RANDINT随机整数
        # 高斯噪声图边缘不做处理，为-1
        ranX = random.randint(0,src.shape[0]-1)
        ranY = random.randint(0,src.shape[1]-1)
        
        # 原灰度图像素值加上随机数
        NoiseImg[ranX,ranY] = NoiseImg[ranX,ranY] + random.gauss(means,sigma)
        
        # 若灰度图小于0赋0，大于255最高为255
        if NoiseImg[ranX,ranY] < 0:
            NoiseImg[ranX,ranY] = 0
        elif NoiseImg[ranX,ranY] > 255:
            NoiseImg[ranX,ranY] = 255
    return NoiseImg

img = cv2.imread("lenna.png",0)
img1 = GaussianNoise(img,2,4,0.8)
img = cv2.imread("lenna.png")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("source", img2)
cv2.imshow("lenna GaussianNoise ", img1)

cv2.waitKey(0)