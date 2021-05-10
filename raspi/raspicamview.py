import cv2 as cv
import numpy as np
from picamera import PiCamera
cap = cv.VideoCapture(-1, cv.CAP_V4L2)
out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=127.0.0.1 port=5000', 0, 30, (224, 224))
 

while True:
    res, frame = cap.read()
    if res:
        re_frame = cv.resize(frame, (224, 224), 0, 0, cv.INTER_LINEAR)
        out.write(re_frame)
        cv.imshow("image", re_frame)
        if cv.waitKey(20) == 27:
            break
                        

cap.release()
out.release()

