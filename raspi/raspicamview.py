from time import time
import cv2 as cv
import numpy as np
import threading
from multiprocessing import Process
#from picamera import PiCamera
from multiprocessing import Process,Value


def sending(temp_time,received):
    frame_count=0 # frame number
    #cap = cv.VideoCapture(-1, cv.CAP_V4L2) # 카메라 모듈에서 영상 받아옴
    #cap = cv.VideoCapture("trailer.mp4") #예시 영상
    filepath = "./trailer.mp4"
    cap = cv.VideoCapture('filesrc location={} ! decodebin ! timeoverlay halignment=right valignment=bottom font-desc="Sans,20" ! videoconvert ! appsink'.format(filepath), cv.CAP_GSTREAMER)
    out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay mtu=1316 ! srtsink uri="srt://:9777?mode=listener"', 0, 30, (224, 224))
    #out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=192.168.0.11 port=9777', 0, 30, (224, 224)) 
    while True:
        res,frame = cap.read()
        if res:
            re_frame = cv.resize(frame, (224,224), 0, 0, cv.INTER_LINEAR)
            # if received.value==1:
            #     with temp_time.get_lock():
            #         temp_time.value=time()
            #     with received.get_lock():
            #         received.value=0
            print(f'Sending Time={time()*100}ms, frmae number={frame_count}')
            out.write(re_frame)
            #cv.imshow("Send", re_frame)
            if cv.waitKey(20) == 27:
                break
    cap.release()
    out.release()
    cv.destroyWindow("send")

def receive(temp_time,received):
    frame_count=0# frame number
    print('before writer open')
    cap =  cv.VideoCapture('srtsrc uri="srt://192.168.0.11:9888?mode=caller" ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER)
    #cap = cv.VideoCapture('udpsrc port=9888 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER)
    print('writer open')
    avg = 0.0
    count = 0
    while True:
        res, frame = cap.read()
        if res:
            # with temp_time.get_lock():
            #     if count > 0 :
            #         avg += (time()-temp_time.value) *100
            #     #print('Receive image Latency : ',(time()-temp_time.value)*100,'ms')
            # with received.get_lock():
            #     received.value=1
            # count += 1
            print(f'Receiving Time={time()*100}ms, frmae number={frame_count}')
            #cv.imshow("receive", frame)
            # if count == 360 :
            #     print('average : %6.2fms' % (avg / count))
            if cv.waitKey(20) == 27:
                break
    cap.release()
    cv.destroyWindow("receive")

#send = threading.Thread(target=sending)
#receive = threading.Thread(target=receive)
#send.start()
#receive.start()
if __name__ == '__main__':
    temp_time=Value('d',0)
    received=Value('d',0)
    s=Process(target=sending,args=(temp_time,received))
    r=Process(target=receive,args=(temp_time,received))
    s.start()
    r.start()
    s.join()
    r.join()
