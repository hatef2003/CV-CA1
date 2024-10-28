from skimage.exposure import cumulative_distribution  
import numpy as np                                    
import matplotlib.pyplot as plt                       
import cv2
def calc_and_draw_hist(image): 
  
    l = image[ : , : image.shape[1]//2]
    r = image[ : , image.shape[1]//2: ]
    histr = cv2.calcHist(r , [0], None , [256], (0,256))
    histl = cv2.calcHist(l , [0], None , [256], (0,256))
    # plt.subplot(1 , 2, 1) 
    # plt.plot(histr)
    # plt.subplot(1 , 2, 2) 
    # plt.plot(histl)
    # plt.show()
def calc_disimilarity(image , template ):
    pixels = np.arange(256)
    cdf_image , bins_image = cumulative_distribution(image)
    cdf_image = np.insert(cdf_image , 0 , [0]*bins_image[0])
    cdf_image = np.append(cdf_image, [1]*(255-bins_image[-1]))

    cdf_template , bins_template = cumulative_distribution(template)
    cdf_template = np.insert(cdf_template , 0 , [0]*bins_template[0])
    cdf_template = np.append(cdf_template, [1]*(255-bins_template[-1]))
    match = np.interp(cdf_image , cdf_template, pixels)
    match = (np.reshape(match[image.ravel()],image.shape)).astype(np.uint8)
    d = np.sum(np.abs(match - image))
    return d

def gray2bin(image , thrsh): 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i , j]> thrsh):
                image[i, j] = 255
            else : 
                image[i , j] = 0
    return image 
pic1 = cv2.imread("MriImages/1.jpeg")
pic1 = cv2.cvtColor(pic1 , cv2.COLOR_RGB2GRAY)
pic2 = cv2.imread("MriImages/2.jpeg")
pic2 = cv2.cvtColor(pic2 , cv2.COLOR_RGB2GRAY)
pic3 = cv2.imread("MriImages/3.jpeg")
pic3 = cv2.cvtColor(pic3 , cv2.COLOR_RGB2GRAY)
pic4 = cv2.imread("MriImages/4.jpeg")
pic4 = cv2.cvtColor(pic4 , cv2.COLOR_RGB2GRAY)
pic5 = cv2.imread("MriImages/5.jpeg")
pic5 = cv2.cvtColor(pic5 , cv2.COLOR_RGB2GRAY)
pic6 = cv2.imread("MriImages/6.jpeg")
pic6 = cv2.cvtColor(pic6 , cv2.COLOR_RGB2GRAY)
pic7 = cv2.imread("MriImages/7.jpeg")
pic7 = cv2.cvtColor(pic7 , cv2.COLOR_RGB2GRAY)
pic8 = cv2.imread("MriImages/8.jpg")
pic8 = cv2.cvtColor(pic8 , cv2.COLOR_RGB2GRAY)








pic1.shape
calc_and_draw_hist(pic1)
calc_and_draw_hist(pic2)
calc_and_draw_hist(pic3)
calc_and_draw_hist(pic4)
calc_and_draw_hist(pic5)
calc_and_draw_hist(pic6)
calc_and_draw_hist(pic7)
calc_and_draw_hist(pic8)

pic1_score = calc_disimilarity(pic1 , pic6)
pic2_score = calc_disimilarity(pic2 , pic6)
pic3_score = calc_disimilarity(pic3 , pic6)
pic4_score = calc_disimilarity(pic4 , pic6)
pic5_score = calc_disimilarity(pic5 , pic6)
pic6_score = calc_disimilarity(pic6 , pic6)
pic7_score = calc_disimilarity(pic7 , pic6)
pic8_score = calc_disimilarity(pic8 , pic6)

print(pic1_score)
print(pic2_score)
print(pic3_score)
print(pic4_score)
print(pic5_score)
print(pic6_score)
print(pic7_score)
print(pic8_score)
thrs = 28543189
# based on thrs 4 5 6 7 has some problem
pic1_bw = gray2bin(pic1 , 128)
pic2_bw = gray2bin(pic2 , 128)
pic3_bw = gray2bin(pic3 , 128)
pic4_bw = gray2bin(pic4 , 128)
pic5_bw = gray2bin(pic5 , 128)
pic6_bw = gray2bin(pic6 , 128)
pic7_bw = gray2bin(pic7 , 128)
pic8_bw = gray2bin(pic8 , 128)