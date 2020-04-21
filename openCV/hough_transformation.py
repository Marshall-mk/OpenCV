import cv2
import numpy as np
""" hough transform is apopular technique to detect any shape,
if you can represent that shape in a mathematical form. it can
detect the shape even if it is broken or distorted a little bit"""
#steps
#Edge detection
#Mapping of edge points to the hough space snd store in an acumulator
# interpretation of the accumulator toyeild lines of infinite lenght
#the interpretation is done by thresholding and other possible constraints
#conversion of infinite lines to finite lines

img = cv2.imread(r'data/sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,50,150,apertureSize=3)
lines = cv2.HoughLines(edge,1,np.pi/180,200)

for line in lines:
	rho,theta = line[0]
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * rho
	y0 = b * rho

	x1 = int(x0 + 1000 * (-b))

	y1 = int(y0 + 1000 * (a))
	x2 = int(x0 - 1000 * (-b))
	y2 = int(y0 - 1000 * (a))
	cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image',img)
cv2.imshow('edge',edge)

cv2.waitKey(0)
cv2.destroyAllWindows() 