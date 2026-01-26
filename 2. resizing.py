#resizing
import os
import cv2

#In this example, we will resize an image using cv2.resize() function.

img = cv2.imread(os.path.join('.','data','bird.jpg'))

resized_img = cv2.resize(img, (300,300)) #width, height

print(img.shape) #(height, width, channels)
print(resized_img.shape) #(height, width, channels)
 
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)  