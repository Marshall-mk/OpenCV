import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'data/lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
Gblur = cv2.GaussianBlur(img,(5,5),0)
median_filter = cv2.medianBlur(img,5) # best for salt and pepper noise
bilateral = cv2.bilateralFilter(img,9,75,75) #egdes are preserved

titles = ['image','2D convolution','blur','GaussianBlur','median_blur','bilateralFilter']
images = [img,dst,blur,Gblur,median_filter,bilateral]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks(ticks=[]),plt.yticks(ticks=[])


plt.show()   