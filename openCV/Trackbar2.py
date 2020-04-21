import cv2
#display current position of trackbar on an image and converts bgr image to gray scale
img = cv2.imread('data/lena.jpg') 
cv2.namedWindow('image')
def nothing(x):
	print(x)
cv2.createTrackbar('CP','image',10,400,nothing) #trackbarname, named window,start point,endpoint,callback 
switch = 'color/gray' # another trackbar
cv2.createTrackbar(switch,'image',0,1,nothing)


while(1):
	img = cv2.imread('data/lena.jpg') 
	pos = cv2.getTrackbarPos('CP','image')# trackbar name,window name
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,str(pos),(50,150),font,4,(0,0,255),10)
	s = cv2.getTrackbarPos(switch,'image')
	k = cv2.waitKey(1)
	if k == 27: #press esc key to quit
		break
	
	if s == 0: # this activates the switch key
		pass
	else:
		img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #says convert to gray 
	img = cv2.imshow('image',img)

cv2.destroyAllWindows() # as usual