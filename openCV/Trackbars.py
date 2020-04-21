import cv2
import numpy as np

#using the positions of bgr trackbars to display corresponding images
def nothing(x): #callback method
    print(x)
img = np.zeros((300,512,3),np.uint8) # creates a black image
cv2.namedWindow('image')
cv2.createTrackbar('B','image',0,255,nothing) #trackbarname, named window,start point,endpoint,callback 
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)
switch = '0 : OFF\n 1 : ON' # another trackbar
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k == 27: #press esc key to quit
        break
    b = cv2.getTrackbarPos('B','image') # trackbar name,window name
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    s = cv2.getTrackbarPos(switch,'image')
    if s == 0: # this activates the switch key
        img[:] = 0
    else:
        img[:] =[b,g,r] #says set the values of bgr to img 
cv2.destroyAllWindows() # as usual