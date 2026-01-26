import cv2
import os

#read video
videoPath = os.path.join('.','data','christmas.mp4')
video = cv2.VideoCapture(videoPath)

#visualize video
ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('Frame', frame)
        cv2.waitKey(50)

video.release() #release video object
cv2.destroyAllWindows() #close all windows