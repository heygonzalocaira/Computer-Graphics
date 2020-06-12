
import cv2
import numpy as np 
from matplotlib import pyplot as plt


img = cv2.imread("log_3.png")
 
height = np.size(img,0)
width = np.size(img,1)

def thresholding(img,h,w,t1,t2):
    for i in range (w-1):
        for j in range (h-1):
            b,r,g=img[j,i]
            temp=int((b+r+g)/3) 
            if (temp >t1 and temp <t2):
                temp = 255
            else:
                temp = 0
            img[j,i] = temp
    cv2.imwrite("t.png",img)

if __name__ == "__main__":

    """
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    """
    thresholding(img,height,width,t1,t2)

