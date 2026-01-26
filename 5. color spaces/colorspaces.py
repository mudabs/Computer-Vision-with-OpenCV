import cv2
import os

# In this example, we will convert an image from BGR to RGB color space using cv2.cvtColor() function.

img = cv2.imread(os.path.join('.', '.', 'data', 'bird.jpg'))
img_gbr = cv2.resize(img, (400, 400))  # width, height

img_rgb = cv2.cvtColor(img_gbr, cv2.COLOR_BGR2RGB) # Convert BGR to RGB
img_gray = cv2.cvtColor(img_gbr, cv2.COLOR_BGR2GRAY)  # Convert to grayscale for demonstration
img_hsv = cv2.cvtColor(img_gbr, cv2.COLOR_BGR2HSV)  # Convert to HSV color space

cv2.imshow('BGR Image', img_gbr)
cv2.imshow('RGB Image', img_rgb)
cv2.imshow('GRAY Image', img_gray)
cv2.imshow('HSV Image', img_hsv)

print('GRAY Image shape:', img_gray.shape)  # Grayscale image has only height and width
print('BGR Image shape:', img_gbr.shape)  # BGR image has height, width, and 3 channels
cv2.waitKey(0)