# Raspberry Pi Files
라즈베리 파이에서 실행할 파일들

## raspicamview.py
최종 테스트에서 실행할 파일.
```
cap = cv.VideoCapture(-1, cv.CAP_V4L2)
```
- 카메라 모듈에서 영상을 받는다.

```
cap = cv.VideoCapture('https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm')
```
- 테스트용 영상
- 추후 로컬 파일을 사용할 수 있도록 수정
