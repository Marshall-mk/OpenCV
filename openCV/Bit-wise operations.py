import cv2
import numpy as np

# perform bit-wise operations on images to obtain a final image(an implementation of truth table)
img = np.zeros((250,500,3),np.uint8) # creates ablack image
img = cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1) # draws a rectangle on the image
img2 = cv2.imread(r'data/image_1.png') # reads a second image

bitAnd = cv2.bitwise_and(img,img2) # performs an AND operation
bitOr = cv2.bitwise_or(img,img2)# OR operation same as truth table
bitXor = cv2.bitwise_xor(img,img2)
bitNot = cv2.bitwise_not(img)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow('img',img)#shows first image
cv2.imshow('img2',img2)#shows a second image
cv2.imshow('bitAnd',bitAnd) # shows the combination(replace the first and  second argument with the intended operation)


cv2.waitKey(0)# waits for the image to be closed
cv2.destroyAllWindows() # as usual