import cv2
import numpy as np
# capturing frames using frames
cap = cv2.VideoCapture(0) #provide either a video file you have or the index of your camera (0 is the default camera,1 is another camera you have)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) # video writer
#while(cap.isOponed()): # executes only if the file or index is True
while(True): #capture continously
    ret, frame = cap.read() #returns true to ret if frame is available and saves it as frame
    if ret == True: # runs only if ret is true
        #gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BGR2GRAY) #to convert the video to gray scale
        cv2.imshow('frame_read',frame) #displays the video being captured
        #cv2.imshow('frame_read',gray) #displays the video being captured as gray scale
        #cap.get(cv2.CAP_PPOP_FRAME_WIDTH) #SHOWS PROPERTIES (HERE THE WIDTH IS SHOWN)
        out.write(frame) # saves the video using the instance defined earlier
        if cv2.waitKey(1) == ord('q'): # if the q key is pressed
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows