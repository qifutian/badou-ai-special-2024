# coding: utf-8

'''
opencv中，Kmeans原型
   retval,bestLabels,centers=kmeans(data,K bestLabels,criteria, attempts, flags[, centers])
'''

import cv2
import numpy as np 

import matplotlib.pyplot as plt

img = cv2.imread("lennna.png",0)
rows,cols = img.shape[:] #获得图像宽高
# 图二维转一维
data=img.reshape((rows*cols,1))
data=np.float32(data)

# 停止条件
criteria = (cv2.TermCriteria_EPS+cv2.TermCriteria_MAX_ITER, 10,1.0)

# 标签设置
flags = cv2.KMEANS_PP_CENTERS

# k-means 聚类，聚4类
compactness,labels,centers = cv2.kmeans(data,4,None, criteria, 10, flags)
# 生成图像
dst=labels.reshape((img.shape[0],img.shape[1]))

# 显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
titles = [u'原始图像', u'聚类图像']  
images = [img, dst]  
for i in range(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray'), 
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()
