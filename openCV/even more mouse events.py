import cv2
import numpy as np

# here we are going to read an image and click a point on the image and it will show the colour of the point clicked in a second window
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1) # draws a circle ofthe given parameters
        img2 = np.zeros((512,512,3),np.uint8)# creates a black image 
        img2[:]=[blue,green,red] # sets the colour to the colour of the clicked point
        cv2.imshow('colour',img2) #shows the image in a second window


img = cv2.imread(r'data/lena.jpg')
cv2.imshow('image',img) #shows the image created
cv2.setMouseCallback('image',click_event) #calls the defined function
cv2.waitKey(0)# waits for the image to be closed
cv2.destroyAllWindows() # as usual