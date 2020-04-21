import cv2
import numpy as np

# The absolute basics
img = cv2.imread(r'data/lena.jpg',1)#to read the images. 1 for coloured RGB,0 for gray scale and -1 for unchanged
#print(img) #prints theoutput as a matrix
cv2.imshow('image',img) #shows the image
#k = cv2.waitKey(5000) # lets us see the image for 5 secs
k = cv2.waitKey(0) #& 0xFF# lets us see the image until we close it
if k == 27:#if the escape key is pressed then execute 
    cv2.destroyAllWindows() # closes/destroys all windows created
elif k == ord('s'):# if the s key is pressed then save
    cv2.imwrite("lena_copy.png",img) #to write an image in form of a file.could be used to change extensions
    cv2.destroyAllWindows()