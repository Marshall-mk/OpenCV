import cv2
import numpy as np
# object detection using hue, saturation and value (HSV)
def nothing(x):
	pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar('LH','Tracking',0,255,nothing) #lower hue
cv2.createTrackbar('LS','Tracking',0,255,nothing)# lower sat
cv2.createTrackbar('LV','Tracking',0,255,nothing) #lower value
cv2.createTrackbar('UH','Tracking',255,255,nothing)
cv2.createTrackbar('US','Tracking',255,255,nothing)
cv2.createTrackbar('UV','Tracking',255,255,nothing)

while True:
	_ ,frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)# converts the image into  hsv format
	
	l_h = cv2.getTrackbarPos('LH','Tracking')
	l_s = cv2.getTrackbarPos('LS','Tracking')
	l_v = cv2.getTrackbarPos('LV','Tracking')
	
	u_h = cv2.getTrackbarPos('UH','Tracking')
	u_s = cv2.getTrackbarPos('US','Tracking')
	u_v = cv2.getTrackbarPos('UV','Tracking')
	

	l_b = np.array([l_h,l_s,l_v]) # lower hsv value for blue
	u_b = np.array([u_h,u_s,u_v])# upper hsv value for blue
	mask = cv2.inRange(hsv,l_b,u_b) #takes values in between the upper and lower limits

	res = cv2.bitwise_and(frame,frame,mask=mask) # AND operation on the image
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('result',res)

	key = cv2.waitKey(1)
	if key == 27: # press esc key to close
		break
cap.release()
cv2.destroyAllWindows() 