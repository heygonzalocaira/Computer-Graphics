import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("mul_4.jpg")
img = img.astype(int)

height = np.size(img,0)
width = np.size(img,1)

c= 7
for i in range(width-1):
    for j in range(height-1):
        a,x,y = img[j,i] 
        a = a*c
        if a > 255:
            a = 255
        x = x*c
        if x > 255:
            x = 255
        y = y*c
        if y > 255:
            y = 255
        img[j,i] = a,x,y

img = img.astype(np.uint8)
#cv2.imshow("Pixel Multiplication",img)
cv2.imwrite("Multiplication2.jpg",img)
cv2.waitKey(0)
