import cv2
import numpy as np


cap = cv2.VideoCapture(r'data/vtest.avi')
ret,frame = cap.read()
x,y,w,h = 300,200,100,50
track_window = (x,y,w,h)
roi = frame[y:y+h,x:x+w]
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,np.array((0.,60.,32.)), np.array((180.,255.,255.,))) 

roi_hist = cv2.calcHist([hsv],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT,10,1)

cv2.imshow('roi',roi)
while (1):
	ret,frame = cap.read()
	if ret == True:

		hsv1 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
		ret, track_window = cv2.CamShift(dst,track_window,term_crit)
		
		pts = cv2.boxPoints(ret)
		pts = np.int0(pts)
		final_image = cv2.polylines(frame,[pts],True,(0,255,0),2)


		
		cv2.imshow('frame',frame)
		cv2.imshow('dst',dst)
		cv2.imshow('final_image',final_image)
		k = cv2.waitKey(30)
		if k == 27:
			break
	else:
		break