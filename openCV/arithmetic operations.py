import cv2
import numpy as np
# perform simple arithmetic operations and a bit photoshop
img = cv2.imread(r'data/messi5.jpg')
img2 = cv2.imread(r'data/opencv-logo.png')
print(img.shape)#returns a tuple of number of rows,colums and channels
print(img.size)# returns Total number of pixels accessed
print(img.dtype)# image datatype

b,g,r = cv2.split(img)
img = v=cv2.merge((b,g,r))

ball = img[280:340,330:390] # says get the ball from this coordinates
img[273:333,100:160] = ball # says place the ball in this coordinates of the original images
img = cv2.resize(img,(512,512)) # resizing images
img2 =cv2.resize(img2,(512,512))
#added_img = cv2.add(img,img2) # to combine two images together you first have to resize them to make sure they are of the same size
added_img = cv2.addWeighted(img,.9,img2,.1,0)# combines in fractions
cv2.imshow('image',added_img) #shows the image created
cv2.waitKey(0)# waits for the image to be closed
cv2.destroyAllWindows() # as usual