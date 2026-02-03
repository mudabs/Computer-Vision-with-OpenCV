import cv2
from PIL import Image
from util import get_limits

# This script captures video from the webcam and detects a specific color (yellow in this case) in real-time.


yellow = [0, 255, 255]  # BGR color for yellow
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(yellow) # get lower and upper limits for yellow color detection
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) # create a mask for yellow color. A mask is a binary image where the detected color regions are white and the rest is black.

    mask_ = Image.fromarray(mask) # convert mask to PIL Image which is required by some libraries for further processing

    bbox = mask_.getbbox()  # get bounding box of the detected color region

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)  # draw rectangle around detected color region    

    cv2.imshow("Mask", mask)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
