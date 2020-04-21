import cv2
import numpy as np

cap = cv2.VideoCapture(r'data/vtest.avi')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorKNN(detectShadows= False)

#fgbg2 = cv2.createBackgroundSubtractorMOG2(detectShadows= False)

while True:
	ret,frame = cap.read()
	if frame is None:
		break
	fgmask = fgbg.apply(frame)
	#fgmask2 = fgbg2.apply(frame)
	cv2.imshow('frame',frame)
	cv2.imshow('fgmask',fgmask)
	#cv2.imshow('fgmask2',fgmask2)

	k = cv2.waitKey(30)
	if k == 'q' or k == 27:
		break




cap.release()
cv2.destroyAllWindows()