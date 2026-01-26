import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # press 'q' to
        break                              #exit    

webcam.release()
cv2.destroyAllWindows()