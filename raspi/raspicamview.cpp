#include <iostream>
#include <raspicam/raspicam_cv.h>
#include <opencv2/imgproc.hpp>
#include <opencv2/opencv.hpp>
  
using namespace cv;
using namespace std;
 

int main()
{
    VideoCapture cap( -1 );
  
    if( !cap.isOpened() ) {
        cout << "Cannot open camera" << endl;
        return 0;
    }

    cv::VideoWriter writer;
    const string pipeline = "appsrc ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=192.168.0.10 port=9777";
    writer.open(pipeline, 0, (double)30, cv::Size(224, 224), true);
    
    if (!writer.isOpened()) {
        printf("=ERR= can't create writer\n");
        return -1;
    }

    cv::Mat frame,re_frame;


    while (true) {
    	cap >> frame;
        resize(frame, re_frame, Size(224, 224), 0, 0, INTER_LINEAR);
	    imshow("Image",re_frame);
        	writer << re_frame;
      	if ( waitKey(20) == 27 ) break; //ESC키 누르면 종료
    }

    return 0;
}

