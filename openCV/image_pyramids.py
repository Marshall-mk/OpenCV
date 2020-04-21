import cv2
import numpy as np
#increasing and decreasing resolutions
#gaussian method
img = cv2.imread('data/lena.jpg') 
layer = img.copy()
gp = [layer]
for i in range(6):
	layer = cv2.pyrDown(layer)
	gp.append(layer)
	#cv2.imshow('rescaled'+str(i),layer)

# lapacian method
layer = gp[5]
cv2.imshow('upper level gaussian pyramid',layer)
lp = [layer]

for i in range(5,0,-1):
	gaussian_extended = cv2.pyrUp(gp[i])
	lapacian = cv2.subtract(gp[i-1],gaussian_extended)
	cv2.imshow(str(i),lapacian)


cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()