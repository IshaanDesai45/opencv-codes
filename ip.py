import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([60,100,70])
    upper_red=np.array([180,255,180])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
   
    
    kernel=np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations=1)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    res =cv2.bitwise_and(frame,frame,mask=closing)
    blur = cv2.GaussianBlur(res,(5,5),0)
    laplacian = cv2.Laplacian(closing,cv2.CV_64F)
   # cv2.imshow('res',res)
    #cv2.imshow('mask',mask)
    #cv2.imshow('hsv',hsv)
   # cv2.imshow('blur',blur)
    #cv2.imshow('erosion',erosion)
    cv2.imshow('closin',closing)
    #cv2.imshow('frame',frame)
   # cv2.imshow('gray',gray)
    cv2.imshow('opening',laplacian)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 



