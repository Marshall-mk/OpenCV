import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'data/smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
# masking is not needed for binary image
kernel = np.ones((2,3),np.uint8)

dilation = cv2.dilate(mask,kernel,iterations = 2)
erosion = cv2.erode(mask,kernel,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
bh = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)


titles = ['image','mask','dilation','erosion','opening','closing','mg','th','bh']
images = [img,mask,dilation,erosion,opening,closing,mg,th,bh]

for i in range(9):
	plt.subplot(2,5,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks(ticks=[]),plt.yticks(ticks=[])


plt.show()   