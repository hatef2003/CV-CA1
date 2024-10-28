import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from conv import convolution
from gaussian_smoothing import gaussian_blur

pic = cv2.imread("grayscale.JPG")
## lap=[-1 -1 -1; -1 8 -1; -1 -1 -1];
 
kernel = np.array([[0, -1, 0 ] ,[-1, 5 ,-1 ], [0, -1, 0 ]])
result = convolution(pic , kernel)
cv2.imwrite("sharpness.jpg" , result)