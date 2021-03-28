#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <stdio.h>
#include <iostream>

using namespace cv;
using namespace std;

int sender(char ip[],char port[]) {
    //TODO 1. 카메라와 연결
    //TODO 2. 영상을 224x224로 리사이징
    // frame
    //TODO 3. 아이피와 포트를 이용 영상을 프레임당 전송
    // stream=Gobject.~~~
    // stream.write()
    
    
    // Windows 10, Visual Studio 2019
	// OpenCV 환경 구성 필요
	
    //TODO 1
	// WebCam 설정
	VideoCapture cap(0, CAP_DSHOW);

	// WebCam 해상도 설정
	cap.set(CV_CAP_PROP_FRAME_WIDTH, 1280);
	cap.set(CV_CAP_PROP_FRAME_HEIGHT, 720);

	// .jpg 파일 이름 설정
	int idx = 0;
	char buff[256];
    
    // WebCam 비활성화 상태일 경우 return
	if (!cap.isOpened())
	{
		printf("Can't open the WebCam");
		return -1;
	}

	Mat frame;
	Mat re_frame;

	while (1)
	{
		cap.read(frame);

		imshow("WebCam Frame Capture", frame);
        
        //TODO 2
		// resizing frame 224 * 224
		resize(frame, re_frame, Size(224, 224), 0, 0, INTER_LINEAR);

		// re_frame(224*224) 저장 (경로 : C:\WebCam\)
        // .jpg 파일 저장 -> WebCam 실행확인용
        // socket programming(IP, PORT), gstreamer 활용하여 re_frame(224*224) 전송 구현 필요
		sprintf_s(buff, "C:\\WebCam\\img_%06d.jpg", idx);
		imwrite(buff, re_frame);

		idx++;
		if (idx == 999999)
			idx = 0;

		// WebCam 종료
		if (waitKey(1) == 27)
			break;
	}
    
    return 0;
}
