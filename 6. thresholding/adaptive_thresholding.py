import os
import cv2

#in this example, we will perform adaptive thresholding on an image using OpenCV.
#adaptive thresholding calculates the threshold for a pixel based on a small region around it.
#this helps in varying lighting conditions.
#use cases include document image binarization, object detection in varying illumination, etc.

img = cv2.imread(os.path.join('.','.','data','thresh_text.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30) # Adaptive thresholding
global_thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY) # Global thresholding for comparison

cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Global Thresholded Image', global_thresh)
cv2.waitKey(0)