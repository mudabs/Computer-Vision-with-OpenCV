import cv2
import os

img = cv2.imread(os.path.join('.','data','bird.jpg'))

cv2.imshow('Original Image', img)
cv2.waitKey(0)