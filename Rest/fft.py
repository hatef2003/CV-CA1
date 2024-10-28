import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("grayscale.JPG")
fft = np.fft.fft2(img[...,1])
fft = np.fft.fftshift(fft)
real = np.real(fft)
img = np.imag(fft)
cv2.imwrite("real.jpg",real)
cv2.imwrite("imag.jpg",img)

