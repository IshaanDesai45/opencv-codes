import numpy as np
import cv2

img =cv2.imread('D:/watch.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,0,0),15)
cv2.rectangle(img,(0,0),(150,150),(255,0,0),5)
cv2.circle(img,(150,150),25,(0,255,0),5)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),5)
  
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllwindows()
