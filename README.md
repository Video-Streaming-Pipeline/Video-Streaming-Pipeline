# Video-Streaming-Pipeline
실시간 이미지 처리 모델을 위한 모바일, 클라우드 영상 전송 파이프라인 개발

## 개발 동기
일반적인 딥러닝 모델(MobileNet 제외)은 컴퓨팅 자원을 많이 요구하기 때문에 모바일이나 마이크로 디바이스에서 실시간으로 사용하기 힘들다.<sup>[1](#1)</sup> 그리고 MobileNet의 경우 가볍지만 성능이 다른 모델보다 낮다.<sup>[2](#2)</sup> 따라서, 고품질의 결과를 위해선 모바일에서 서버에 실시간으로 빠르게 영상을 전송하는 프레임워크가 필요하다.

## 목표
1. 모바일과 클라우드 모델을 실시간으로 연결하는 파이프라인을 개발한다.
2. 빠른 네트워크(5G 등)를 이용해서 클라우드 기반 모델이 모바일 기반 모델(MobileNet)만큼 빠른 속도로 서비스를 제공 할 수 있음을 증명한다.

## Reference
<a name="1">1</a>. Deep Learning Inference Benchmarks, https://developer.nvidia.com/embedded/jetson-nano-dl-inference-benchmarks<br>
<a name="2">2</a>. ImageNet 1-crop error rates (224x224), https://pytorch.org/vision/stable/models.html#classification
