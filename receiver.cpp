#include <opencv/build/include/opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;


int receiver(){
    //TODO 1. 인풋 스트림을 열어서
    // stream = Gobject.~~~
    // frame = stream.read()
    //TODO 2. 수신 받은 걸 openCV에 쓸 수 있도록 가공

    //TODO 3. openCV에서 돌려서 결과출력
    Mat frame;

    while(true) {

        cap.read(frame);

        if(frame.empty())
            break;

        imshow("Receiver", frame);
        if(waitKey(1) == 'r')
            break;
    }
    destroyWindow("Receiver");
}