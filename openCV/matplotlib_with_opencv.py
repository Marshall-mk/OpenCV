import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'data/lena.jpg',-1)
cv2.imshow('image',img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #matplotlib takes images as rbg
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()