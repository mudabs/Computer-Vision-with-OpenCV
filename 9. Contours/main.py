import cv2
import os

# in this example, we will detect contours in an image using OpenCV.
# contours are curves joining all the continuous points along a boundary which have the same color or intensity


img = cv2.imread(os.path.join('.', '.', 'data', 'many_birds.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) # Global thresholding with binary inverse meaning pixels below threshold are set to max value

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find contours

for cnt in contours:
    if (cv2.contourArea(cnt)) > 200:
        # cv2.drawContours(img, [cnt], -1, (0, 255, 0), 1) # Draw contours with area greater than 200 on the original image
        x1, y1, w, h = cv2.boundingRect(cnt) # Get bounding box coordinates 
        cv2.rectangle(img, (x1,y1), (x1+w,y1+h), (0,255,0), 1) # Draw bounding box around contours with area greater than 200

cv2.imshow('Many Birds', img)
cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)