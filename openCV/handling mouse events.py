import cv2
import numpy as np

# Give position of mouse on an image and the bgr channels

def click_event(event,x,y,flags,param): #
    if event == cv2.EVENT_LBUTTONDOWN:# gives the position of the mouse when the left button is clicked on an image
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) +','+str(y)
        cv2.putText(img,strXY,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('image',img)
    elif event == cv2.EVENT_RBUTTONDOWN: # gives the bgr channels when the right key is pressed
        blue = img[x,y,0 ]
        green = img[x,y, 1]
        red = img[x,y,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strbgr = str(blue) +','+str(green)+ ','+str(red)
        cv2.putText(img,strbgr,(x,y),font,.5,(0,255,255),2)
        cv2.imshow('image',img)
img = cv2.imread(r'data/lena.jpg')
#img = np.zeros([512,512,3],np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()