import os
import cv2

img = cv2.imread(os.path.join('.','.','data','man.jpg'))
k_size = 7 # Kernel size for blurring

#Ordinary Blurring
img_blur = cv2.blur(img,(k_size, k_size)) # Apply average blurring 

#Gaussian Blurring
img_gaussian = cv2.GaussianBlur(img,(k_size, k_size),5) # Apply Gaussian blurring with sigma=5 meaning how much the blur spreads

#Median Blurring    
img_median = cv2.medianBlur(img, k_size) # Apply Median blurring

cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', img_blur)
cv2.imshow('Gaussian Blurred Image', img_gaussian)
cv2.imshow('Median Blurred Image', img_median)
cv2.waitKey(0) 