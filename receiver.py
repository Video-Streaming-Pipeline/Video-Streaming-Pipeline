import cv2 as cv
import numpy as np

cap = cv.VideoCapture('udpsrc port=9777 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER)

if not cap.isOpened():
    print("VideoCapture not opened")
    exit(-1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("empty frame")
        break
    cv.imshow("Receiver", frame)
    if cv.waitKey(1) == 'r':
        break

cap.release()
cv.destroyWindow("Receiver")