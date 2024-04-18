
# 工作中直接用

import numpy as np
from PLL import Image
from skimage import util

# def random_noise(image,mode="gaussian,seed=none,clip=True, **kwargs")

img = cv.imread("lenna.png")
noise_gs_img = util.random_noise(img,mode='poisson')

cv.imshow("source",img)
cv.imshow("lenna",noise_gs_img)
cv.waitkey(0)
cv.destroyAllWindows()
