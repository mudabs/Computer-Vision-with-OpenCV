import os
import cv2

#in this example, we will perform global thresholding on an image using OpenCV.
#global thresholding applies a single threshold value to the entire image.
#use cases include simple background-foreground segmentation, basic image binarization, etc.

img = cv2.imread(os.path.join('.','.','data','bear.jpg'))
img_resize = cv2.resize(img, ( 1200, 800))  # width, height

img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY) # Global thresholding at 80 value where ret is the threshold used meaning 80 in this case
thresh_blur = cv2.blur(thresh, (10,10))

cv2.imshow('Original Image', img_resize)
cv2.imshow('Thresholded Image', thresh_blur)
cv2.waitKey(0)