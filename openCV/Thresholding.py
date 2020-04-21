import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('data/sudoku.png',0) 
_ , th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # the image,threshold value,maximum value ,dtype
# if the pixel value is less then 127 then assign to 0(black).

_ , th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) # the inverse thresh_binary.(<127=1)
_ , th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # all pixels less than threshold doesnt change, those above threshold are assigned to threshold 
_ , th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # all pixels less than threshold change to zero, those above threshold are unchanged
_ , th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) # all pixels less than threshold are unchangeg, those above threshold are changed to zero
#adaptive thresholding
#th6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#th7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['original image','binary','binary_inv','truc','tozero','tozero_inv']
images = [img,th1,th2,th3,th4,th5]


for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])


#cv2.imshow('image',img)
#cv2.imshow('image1',th1)
#cv2.imshow('image2',th2)
#cv2.imshow('image3',th3)
#cv2.imshow('image4',th4)
#cv2.imshow('image5',th5)
#cv2.imshow('image6',th6)
#cv2.imshow('image7',th7)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows() # as usual