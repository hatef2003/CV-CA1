from skimage.io import imread                         
from skimage.exposure import cumulative_distribution  
import numpy as np                                    
import matplotlib.pyplot as plt                       
import cv2

pixels = np.arange(256)
near = cv2.imread("near.jpg")
far = cv2.imread("far.jpg")
deg = cv2.imread('45deg.jpg')
mask = cv2.imread('mask.jpg')
near = cv2.cvtColor(near , cv2.COLOR_RGB2GRAY)
far = cv2.cvtColor(far , cv2.COLOR_RGB2GRAY)
deg = cv2.cvtColor(deg , cv2.COLOR_RGB2GRAY)
mask = cv2.cvtColor(mask , cv2.COLOR_RGB2GRAY)

cdf_near , bins_near = cumulative_distribution(near)
cdf_far , bins_far = cumulative_distribution(far)
cdf_deg , bins_deg = cumulative_distribution(deg)
cdf_mask , bins_mask = cumulative_distribution(mask)
cdf_near = np.insert(cdf_near , 0 , [0]*bins_near[0])
cdf_far = np.insert(cdf_far , 0 , [0]*bins_far[0])
cdf_deg = np.insert(cdf_deg , 0 , [0]*bins_deg[0])
cdf_mask = np.insert(cdf_mask , 0 , [0]*bins_mask[0])
cdf_near = np.append(cdf_near, [1]*(255-bins_near[-1]))
cdf_far = np.append(cdf_far, [1]*(255-bins_far[-1]))
cdf_deg = np.append(cdf_deg, [1]*(255-bins_deg[-1]))
cdf_mask = np.append(cdf_mask, [1]*(255-bins_mask[-1]))
far_near = np.interp(cdf_far , cdf_near, pixels)
far_far = np.interp(cdf_far , cdf_far, pixels)
far_deg = np.interp(cdf_far , cdf_deg, pixels)
far_mask = np.interp(cdf_far , cdf_mask, pixels)
far_near = (np.reshape(far_near[far.ravel()],far.shape)).astype(np.uint8)
far_far = (np.reshape(far_far[far.ravel()],far.shape)).astype(np.uint8)
far_deg = (np.reshape(far_deg[far.ravel()],far.shape)).astype(np.uint8)
far_mask = (np.reshape(far_mask[far.ravel()],far.shape)).astype(np.uint8)
cv2.imshow("1",far_near)
cv2.waitKey()
cv2.imshow("1",far_far)
cv2.waitKey()
cv2.imshow("1",far_deg)
cv2.waitKey()
cv2.imshow("1",far_mask)
cv2.waitKey()
def calc_cdf(image) :
   bin, hist = np.histogram(image)
   return hist.cumsum()

dissimilarity_near = np.sum(np.abs(far_near - far))
dissimilarity_far = np.sum(np.abs(far_far - far))
dissimilarity_deg = np.sum(np.abs(far_deg-far))
dissimilarity_mask = np.sum(np.abs(far_mask-far))


print(dissimilarity_near)
print(dissimilarity_far)
print(dissimilarity_deg)
print(dissimilarity_mask)

