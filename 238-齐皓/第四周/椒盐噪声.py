
import numpy as np
import cv2
from numpy import shape
import random

def fun1(src, percetage):
    NoiseImg = src
    NoiseNum = int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        # 每次去的一个随机点
        # 一张图片用行列表示，randX随机行，ranY随机列
        # random.RANDINT随机整数
        # 噪声图边缘不做处理，为-1
        ranX = random.randint(0,src.shape[0]-1)
        ranY = random.randint(0,src.shape[1]-1)
        
        # random.random生成随机浮点数，随意渠道一个像素点有一半的可能是白点255
        if random.random() <= 0.5:
            NoiseImg[ranX,ranY] = 0
        else:
            NoiseImg[ranX,ranY] = 255
    return NoiseImg

img = cv2.imread("lenna.png",0)
img1 = fun1(img,0.2)


img = cv2.imread("lenna.png")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("source", img2)
cv2.imshow("lenna GaussianNoise ", img1)

cv2.waitKey(0)