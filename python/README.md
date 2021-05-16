# Abstract
Pytorch를 이용해서 이미지 처리와 관련된 모델들을 GPU 또는 CPU에서 실행하고 수행능력을 파악 할 수 있다.

# Requirement
1. [install pytorch with cuda-toolkit](https://pytorch.org/get-started/locally/) (라즈베리파이의 경우 pytorch만 설치)

2. install torchvision
```
pip install torchvision
```
# Usage
```
python benchmark.py
```
- 로컬에서 여러 모델을 실행시 평균 추론시간을 계산 할 수 있다.
- 기본적으로 CPU를 사용하며 GPU를 사용할 수 있는 환경인 경우 GPU를 사용하여 연산한다.

```
python benchmark_with_streaming.py
```
- 스트리밍을 통해 입력받은 모델에서 객체 탐지를 수행한다. -> 개선된 모델로 추가 예정
- 스트리밍시 프레임당 추론시간을 출력한다. (평균 추론 시간을 구하고 싶다면 benchmark.py를 사용하도록 한다.)
- 현재 데모 영상을 사용하고 있으며 라즈베리파이에서 수신하기 위해서는 VideoCapture를 다음과 같이 변경해야한다.

현재
```python
cap = cv.VideoCapture('https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm')
```

변경
```python
cap = cv.VideoCapture('udpsrc port=9777 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink', cv.CAP_GSTREAMER)
```
- 라즈베리파이와 연동시 네트워크 에뮬레이터를 통해서 4G 또는 5G의 환경을 조성해서 실행하도록한다.
- 서버에서 다시 라즈베리파이로 영상을 보내는 경우는 아직 구현되어 있지 않다.

# 목표
라즈베리파이와 본 과제의 결과를 비교하여 라즈베리파이의 한계를 극복했다는 것을 증명한다.

- 정확성 차이를 수치 및 영상으로 보여주어 중요성 강조 -> 이건 이미 대부분 증명되어 있으므로 다른 자료 참조
ex.)
![image](https://user-images.githubusercontent.com/30094719/118394281-ad073f80-b67e-11eb-87c5-ffd4e8326927.png)

- 본 과제를 통한 결과와 기존 라즈베리파이의 성능 비교
  - 수치의 경우 benchmark.py를 사용
  - 영상의 경우 benchmark_with_streaming.py를 사용  ex) https://youtu.be/P5OGv9pt_Mc?t=16
