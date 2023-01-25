# Import Libraries

import numpy as np

import cv2

import time
# camCount=0
#To use webcam  enter 0 and to enter the video path in dowble quotes
cap = cv2.VideoCapture(0)

time.sleep(3)

background = 0


# Capturing the background
for i in range(60):

    ret, background = cap.read()
#capturing image
background = np.flip(background,axis=1)
while(cap.isOpened()):

    ret, img = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #HSV values

    #setting the values for the cloak
    lower_red = np.array([255,0,0])
    upper_red = np.array([255,0,0])

    #lower_red = np.array([110, 50, 50])
    #upper_red = np.array([130, 255, 255])


    mask1 = cv2.inRange(hsv, lower_red,upper_red)

    lower_red = np.array([170,120,70])
    upper_red =  np.array([180,255,255])

    #lower_red = np.array([150, 150, 0])
    #upper_red = np.array([180, 255, 255])




    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1 +mask2

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    mask2 =cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background,background,mask=mask1)
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Cloak',final_output)
    k = cv2.waitKey(10)    
    if k =="q":
        break
cap.release()
cv2.destroyAllWindows()