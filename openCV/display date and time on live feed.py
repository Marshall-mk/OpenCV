import cv2
import numpy as np
import datetime as dt

# show date and time on live feed
cap = cv2.VideoCapture(0) #provide either a video file you have or the index of your camera (0 is the default camera,1 is another camera you have)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) # video writer
#cap.get(3)#width
#cap.set(3,1080)# changes the default width
#cap.set(4,720)# changes the default height

while(True): # executes only if the file or index is True
    ret, frame = cap.read() #returns true to ret if frame is available and saves it as frame
    if ret == True: # runs only if ret is true
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:'+str(cap.get(3)) + ' Height:'+str(cap.get(4))
        datet= str(dt.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)

        cv2.imshow('frame_read',frame) #displays the video being captured
     
        out.write(frame) # saves the video using the instance defined earlier
        if cv2.waitKey(1) == ord('q'): # if the q key is pressed
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows