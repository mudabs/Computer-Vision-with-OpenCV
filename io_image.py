import os
import cv2

#read image
image_path = os.path.join('.', 'data', 'bird.jpg') #Constructs the file path to the image
img = cv2.imread(image_path) #Reads the image from the specified path

#write image

cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img) #Saves the image to a new file

#visualize image
cv2.imshow('Frame', img) #Displays the image in a window
cv2.waitKey(0) #Keeps the window open until a key is pressed


