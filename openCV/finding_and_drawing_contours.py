import cv2
import numpy as np
#contours are curves joining all continues point along the boundry having same intensity(colour)
#useful for object detection/recognition and shape analysis
img = cv2.imread('data/opencv-logo.png') 
imgray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print('Number of contours = ',len(contours))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),3)# -1 draws all the contours(3rd argument)

cv2.imshow('Image',img)
cv2.imshow('Image gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()