import numpy as np
import cv2
import colorsys
image = cv2.imread('Color.JPG')
normalled_image = image.astype(float)/255.
K =( 1 - np.max(normalled_image, axis=2))
C = ((1-normalled_image[...,2] - K)/(1-K)) * 255
M = ((1-normalled_image[...,1] - K)/(1-K)) * 255
Y = ((1-normalled_image[...,0] - K)/(1-K)) * 255
K *=255
CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
cv2.imwrite("CYK/C.jpg" ,C.astype(np.uint8))
cv2.imwrite("CYK/M.jpg" ,M.astype(np.uint8))
cv2.imwrite("CYK/Y.jpg" ,Y.astype(np.uint8))
cv2.imwrite("CYK/K.jpg" ,K.astype(np.uint8))
R = image[... ,0]/255
G = image[... ,1]/255
B = image[... ,2]/255
H = np.zeros(R.shape , like=R)
S = np.zeros(R.shape , like=R)
L = np.zeros(R.shape , like=R)
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        hls = colorsys.rgb_to_hls(R[i,j] , G[i , j] , B[i , j])
        H[i , j ]= hls[0]*255
        L[i , j ]= hls[1]*255
        S[i , j ]= hls[2]*255
cv2.imwrite("HLS/H.jpg" ,M.astype(np.uint8))
cv2.imwrite("HLS/L.jpg" ,Y.astype(np.uint8))
cv2.imwrite("HLS/S.jpg" ,K.astype(np.uint8))