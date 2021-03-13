# Video-Streaming-Pipeline
실시간 이미지 처리 모델을 위한 모바일, 클라우드 영상 전송 파이프라인 개발

## 개발 동기
근래의 이미지 처리CNN 모델(MobileNet 제외)은 컴퓨팅 자원을 많이 요구하기 때문에 모바일이나 마이크로 디바이스에서 실시간으로 사용하기 힘들다.<sup>[[1]](#1)</sup><sup>[[3]](#3)</sup> 그리고 MobileNet의 경우 지연율이 낮지만 다른 모델보다 낮다.<sup>[[2]](#2)</sup><sup>[[3]](#3)</sup> 따라서, 고품질의 정확도를 위해선 단말에서 서버에 실시간으로 빠르게 영상을 전송하는 프레임워크가 필요하다. 또한 5G의저지연을 이용하면 단말에서 수행하는 것과 유사한 결과를 얻을 수 있을 가능성이 있다.

## 목표
1. 모바일에서 클라우드 모델로 영상을 실시간으로 전송하는 파이프라인을 개발한다.
2. 빠른 네트워크(5G 등)를 이용해서 클라우드 기반 모델이 모바일 기반 모델(MobileNet)만큼 빠른 속도로 서비스를 제공 할 수 있음을 증명한다.

## Reference
 <a name="1">1</a>. Table 1. Inference performance results from Jetson Nano, Raspberry Pi 3, Intel Neural Compute Stick 2, and Google Edge TPU Coral Dev Board, https://developer.nvidia.com/embedded/jetson-nano-dl-inference-benchmarks<br>
 <a name="2">2</a>. Image Classification on ImageNet, https://paperswithcode.com/sota/image-classification-on-imagenet<br>
 <a name="3">3</a>. Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, Hartwig Adam, MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications, https://arxiv.org/abs/1704.04861
