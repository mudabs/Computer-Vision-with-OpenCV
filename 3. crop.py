import cv2
import os

#In this example, we will crop an image using array slicing.

img = cv2.imread(os.path.join('.','data','bird.jpg'))

print(img.shape) #(height, width, channels)
cropped_img = img[450:2000, 0:1440] #y1:y2, x1:x2

cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)