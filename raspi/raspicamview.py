import cv2 as cv
import numpy as np
import threading
from multiprocessing import Process
from picamera import PiCamera
 
def sending():
    # cap = cv.VideoCapture(-1, cv.CAP_V4L2) # 카메라 모듈에서 영상 받아옴
    cap = cv.VideoCapture('https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm') # 테스트 영상
    out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=221.164.144.187 port=9777', 0, 30, (224, 224))
    while True:
        res,frame = cap.read()
        if res:
            re_frame = cv.resize(frame, (224,224), 0, 0, cv.INTER_LINEAR)
            out.write(re_frame)
            cv.imshow("Send img", re_frame)
            if cv.waitKey(20) == 27:
                break

def receive():
    print('before writer open')
    cap = cv.VideoCapture('udpsrc port=9888 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER)
    print('writer open')
    while True:
        res, frame = cap.read()
        if res:
            cv.imshow("Receive img", frame)    
            if cv.waitKey(20) == 27:
                break
                        
#send = threading.Thread(target=sending)
#receive = threading.Thread(target=receive)
#send.start()
#receive.start()
if __name__ == '__main__':
    s=Process(target=sending)
    r=Process(target=receive)
    s.start()
    r.start()
    s.join()
    r.join()
