'''
라즈베리파이에서 서버로 영상을 전송하는 과정은 Raspicamview.py과 동일
단, 수신의 경우 객체 탐지 모델의 Bounding Box정보(int:4,double:1)만 받도록 함

@Main Author : BEOKS(lee01042000@gmail.com)
'''

from multiprocessing.synchronize import SemLock
from multiprocessing import Process
from time import time
import cv2 as cv
import numpy as np
import threading
import socket,pickle

'''
seding의 경우 raspicamview.py와 동일
'''
def sending():
    frame_count=0 # frame number
    filepath = "./trailer.mp4"
    cap = cv.VideoCapture('filesrc location={} ! decodebin ! timeoverlay halignment=right valignment=bottom font-desc="Sans,20" ! videoconvert ! appsink'.format(filepath), cv.CAP_GSTREAMER)
    out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay mtu=1316 ! srtsink uri="srt://:9777?mode=listener"', 0, 30, (224, 224))
    #out = cv.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=192.168.0.11 port=9777', 0, 30, (224, 224)) 
    while True:
        res,frame = cap.read()
        if res:
            re_frame = cv.resize(frame, (224,224), 0, 0, cv.INTER_LINEAR)
            print(f'Sending Time={time()*100}ms, frmae number={frame_count}')
            frame_count+=1
            out.write(re_frame)
            #cv.imshow("Send", re_frame)
            if cv.waitKey(20) == 27:
                break
    cap.release()
    out.release()
    cv.destroyWindow("send")
'''
서버에서 보낸 클래스를 받아서 디코딩 후 이를 반환함
'''
def receive():
    frame_number=0
    ip='192.168.0.11'
    port=9778
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clinet_socket:
        clinet_socket.connect((ip,port))
        while True:
            clinet_socket.send(b'ready')
            data=clinet_socket.recv(4096)
            if not data:#null data received
                print('Receiving Prcoess finished')
                break
            print(f'Receiving Time={time()*100}ms,Frame Number : {frame_number}')
            frame_number+=1
            data=pickle.loads(data)
            print(data)
            


if __name__ == '__main__':
    s=Process(target=sending)
    r=Process(target=receive)
    s.start()
    r.start()
    s.join()
    r.join()
