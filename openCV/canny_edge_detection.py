import cv2
import numpy as np
from matplotlib import pyplot as plt
# edge detector that uses a multi stage algorithm to detect a wide range of edges in images 

# steps
#noise reduction
#gradient calculation
#non-maximum suppression
#doube threshold
#edge tracking by hysterisis

img = cv2.imread('data/messi5.jpg',0) 
canny = cv2.Canny(img,100,200)


titles = ['image','canny']
images = [img,canny]




for i in range(len(images)):
	plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()