import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('hist6.jpg')
img_shape = img.shape
height = img_shape[0]
width = img_shape[1]
""" 
for row in range(width):
    for column in range(height):
        print(img[column][row])

"""
def get_histogram(image, bins):
    # array with size of bins, set to zeros
    histogram = np.zeros(bins)
    
    # loop through pixels and sum up counts of pixels
    for pixel in image:
        histogram[pixel] += 1
    
    # return our final result
    return histogram
img = cv.imread('hist5.jpg')
hist = get_histogram(img, 256)
plt.hist(img.ravel(),256,[0,256]); plt.show()

###############
