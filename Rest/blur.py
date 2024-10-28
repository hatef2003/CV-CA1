import numpy as np
import cv2
import matplotlib.pyplot as plt
from conv import convolution
# from gaussian_smoothing import gaussian_blur
avg_kernel = np.array([[1,1,1,1,1] , [1,1,1,1,1], [1,1,1,1,1] , [1,1,1,1,1],[1,1,1,1,1] ])
image = cv2.imread("grayscale.JPG")
avg_blur = convolution(image, avg_kernel , True)
cv2.imwrite("avg_blur.jpg" , avg_blur)
gussian_kernel = np.array([[1,4,6,4,1],[4,16,24,16,4] ,[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
gussian_blur = convolution(image , gussian_kernel , True)
cv2.imwrite("gussain_blur.jpg" , gussian_blur)
