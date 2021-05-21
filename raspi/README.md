# Raspberry Pi Files
라즈베리 파이에서 실행할 파일들

## raspicamview.py
최종 테스트에서 실행할 파일.
```
cap = cv.VideoCapture(-1, cv.CAP_V4L2)
```
- 카메라 모듈에서 영상을 받는다.

```
cap = cv.VideoCapture('trailer.mp4')
```
- 테스트용 영상(trailer.mp4) 사용
- 같은 영상을 사용함으로써 변인을 통제한다.
