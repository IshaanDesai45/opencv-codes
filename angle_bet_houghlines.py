import cv2
import numpy as np
 
video = cv2.VideoCapture("D:/path.mp4")
 
while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("path.mp4")
        continue
    z=np.pi/180
    frame = cv2.GaussianBlur(orig_frame, (15, 15), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([0, 135, 80])
    up_yellow = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    edges = cv2.Canny(mask, 75, 150)
    cv2.imshow("mask",mask)
 
    lines = cv2.HoughLines(edges, 1,z,  200)
    #print(lines[0])
    if lines is not None:
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            print(theta/z)
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
           
            
            
 
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
 
    key = cv2.waitKey(25)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
