import cv2
import numpy as np
import matplotlib.pyplot as plt
def roi(img,vertices):
	mask = np.zeros_like(img)
	#channel_count = img.shape[2]
	match_mask_color = 255
	cv2.fillPoly(mask,vertices,match_mask_color)
	masked_image = cv2.bitwise_and(img,mask)
	return masked_image

def draw_lines(img,lines):
	img = np.copy(img)
	line_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),thickness = 3)
	img = cv2.addWeighted(img, 0.8,line_image,1,0.0)
	return img

#img = cv2.imread(r'data/road1.jpeg')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
def process(img):
	print(img.shape)
	h = img.shape[0]
	w = img.shape[1]

	roiv = [(0,h),(w/2,h/2),(w,h)]
	gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	canny = cv2.Canny(gray,100,120)
	croped = roi(canny,np.array([roiv],np.int32),)

	lines = cv2.HoughLinesP(croped,rho=2,theta=np.pi/60,threshold=50,lines=np.array([]),minLineLength=40,maxLineGap=25)
	images_with_lines = draw_lines(img,lines)
	return images_with_lines

cap = cv2.VideoCapture(r'data/test.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()
	frame = process(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()