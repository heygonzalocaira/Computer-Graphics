import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('question_2.png')

height = np.size(img, 0)
width = np.size(img, 1)
img2 = np.zeros((height,width,1),np.uint8)

for i in range (width-1):
    for j in range (height-1):
        b,r,g=img[j,i]
        temp=int((b+r+g)/3)
        if(b<=255 and b>=50):
            temp=255
        else:
            temp=1
        img[j,i]=temp

cv2.destroyAllWindows()
cv2.imwrite('salida2.png',img)


