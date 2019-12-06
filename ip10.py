import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original',frame)
    edges = cv2.Canny(grayscaled,150,200)
    cv2.imshow('Edges',edges)
    cv2.imshow('mask',mask)
    cv2.imshow('mask',res)
    cv2.waitKey(5)
    

cv2.destroyAllWindows()
cap.release()
