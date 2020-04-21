import cv2
import numpy as np

# draw geometric shapes
path = r'data/'
#img = cv2.imread(path+'lena.jpg',-1)
img = np.zeros([512,512,3],np.uint8)
#img = cv2.line(img,(0,0),(255,255),(255,255,0),5)# draws a line with the given parameters
#the image itself,the start point,end point,color,thickness (-1 fills it with the colour provided)
#img = cv2.arrowedLine(img,(0,255),(0,255),(255,255,0),5) # for arrowed line
#img = cv2.rectangle(img,(0,0),(255,255),(255,255,0),5) #draws a rectangle
img = cv2.circle(img,(447,63),63,(0,255,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img,'this is my first time',(30,100),font2,2,(0,255,255),10,cv2.LINE_AA )
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()