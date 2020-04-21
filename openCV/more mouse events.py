import cv2
import numpy as np

# draw and join points on an image

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1) # draws a circle ofthe given parameters
        points.append((x,y))# appends the points clicked to the  list
        if len(points)>=2: # checks the lenght of the list to be >= 2
            cv2.line(img,points[-1],points[-2],(255,0,0),5) #joins the last two points using a line

        cv2.imshow('image',img) #shows the image


#img = cv2.imread(r'data/lena.jpg')
img = np.zeros([512,512,3],np.uint8) #creates the image using numpy arrays
cv2.imshow('image',img) #shows the image created
points =[] #the empty list where values will be appended
cv2.setMouseCallback('image',click_event) #calls the defined function
cv2.waitKey(0)# waits for the image to be closed
cv2.destroyAllWindows() # as usual