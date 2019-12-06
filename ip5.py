import cv2
import numpy as np
img1= cv2.imread('D:/3D-matplotlib.png',cv2.IMREAD_COLOR)
img2= cv2.imread('D:/mainsvmimage.png',cv2.IMREAD_COLOR)
#add=img1+img2
#add = cv2.add(img1,img2)
add= cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow('add',add)
cv2.namedWindow('add',cv2.WINDOW_NORMAL)
cv2.resizeWindow('add',600,600)
