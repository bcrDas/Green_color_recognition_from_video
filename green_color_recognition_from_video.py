#Green color recognition from video:-

import cv2
import numpy as np

vidcap = cv2.VideoCapture('videoplayback.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
    success,image = vidcap.read()
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1


    lower_red=np.array([29,86,6])
    upper_red=np.array([64,225,225])
    
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(image,image,mask=mask)
    
    #kernel=np.ones((15,15),np.float32)/225
    #smoothed=cv2.filter2D(res,-1,kernel)
    
    #blur=cv2.GaussianBlur(res,(15,15),0)
    
    cv2.imshow('image',image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.imshow('smoothed',smoothed)
    #cv2.imshow('blur',blur)
    
    
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindow()
cap.relese()
