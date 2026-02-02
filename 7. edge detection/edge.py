import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.','.','data','basketball.jpg'))

img_edge = cv2.Canny(img, 100, 200) # Canny Edge Detection
img_edge_d = cv2.dilate(img_edge, np.ones((3,3), dtype=np.int8)) #dilate edges to make them more visible
img_edge_e = cv2.erode(img_edge_d, np.ones((3,3), dtype=np.int8)) 

cv2.imshow('Original Image', img)
cv2.imshow('Edge Image', img_edge)
cv2.imshow('Edge Image Dilated', img_edge_d)
cv2.imshow('Edge Image Eroded', img_edge_e)
cv2.waitKey(0)