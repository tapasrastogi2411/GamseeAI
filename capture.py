import cv2
import numpy as np
import time

# Object for video capturing
# Passing value '0' or '-1' is for first (default) external camera (webcam)
# Passing value '1' is for second external camera
video = cv2.VideoCapture(0)

# Variable 'milliSeconds' represents the streamed milliseconds
milliSeconds = 0

# Video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
output = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# Loop stream
while True:
    milliSeconds = milliSeconds + 1
    ret, frame = video.read()

    print(ret) # print recognition in array format
    print(frame) # print image representation

    # Display video in grayscale real-time
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Frame output
    output.write(frame)

    # Display frame real-time
    cv2.imshow("OpenCV", frame)

    # User controls
    ctrlAbort = cv2.waitKey(1)

    if ctrlAbort == ord('z'):
        break

video.release()
output.release()
print(milliSeconds)

video.release()
cv2.destroyAllWindows