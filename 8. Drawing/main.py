import os
import cv2


image_path = os.path.join('.', 'data', 'whiteboard.jpg') 
img = cv2.imread(image_path) 

#Drawing a line
#line
cv2.line(img, (100,150), (300,450), (255,0,0), 3)  #line from (100,150) to (300,450) with blue color and thickness 3

#rectangle
cv2.rectangle(img, (400,100), (600,400), (0,255,0), -1) #filled rectangle
cv2.rectangle(img, (100,150), (300,450), (0,0,255), 3)  #line rectangle

#circle
cv2.circle(img, (700,300), 50, (0,0,255), -1) #filled circle

#text
cv2.putText(img, 'Hey you!',(90, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

cv2.imshow('Frame', img) 
cv2.waitKey(0) 


