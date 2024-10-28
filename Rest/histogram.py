import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("grayscale.JPG")
hist = cv2.calcHist(img[...,1],[0] , None , [256],(0,256))
plt.subplot(1,2,1)
plt.plot(hist)
img = cv2.equalizeHist(img[...,1])
cv2.imshow("a", img)
cv2.waitKey()
hist2 = cv2.calcHist(img,[0] , None , [256],(0,256))
plt.subplot(1 , 2 ,2)
plt.plot(hist2)
plt.show()
rgb_im = cv2.imread("Color.JPG")
histr = cv2.calcHist(rgb_im , [0], None , [256], (0,256))
histg = cv2.calcHist(rgb_im , [1], None , [256], (0,256))
histb = cv2.calcHist(rgb_im , [2], None , [256], (0,256))
plt.plot(histr , color = "red", label = "red")
plt.plot(histg , color = "green", label = "green")
plt.plot(histb , color = "blue", label = "blue")
plt.legend() 
plt.show()