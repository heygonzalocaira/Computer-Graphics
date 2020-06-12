import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread("question_1.png")

img_out = img

height = np.size(img, 0)
width = np.size(img, 1)

c = 88

b = 1.01

for x in range(width-1):
    for y in range (height-1):
        B,G,R = img[y,x]
        temp = c * (pow(b,B) - 1)
        if(temp > 255):
            temp = 255
        if(temp < 0):
            temp = 0
        img[y,x] = temp


######## the Rsult have to B set in img_out ####
######## not modify from heR ####################

cv2.imwrite("salida_1.png", img_out)
