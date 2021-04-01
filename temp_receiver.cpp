#include <opencv2/opencv.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>

#include <stdio.h>

using namespace cv;
using namespace std;
int main(int argc, const char * argv[]) {

//    int sock;
//    struct sockaddr_in serv_addr;//주소
//    FILE *file = NULL; // 전송할 파일
//    size_t fsize = 0, nsize = 0, fpsize = 0;
//    size_t fsize2 = 0;
//    char file_buf[256];
//    memset(file_buf,0,256);
//
//    sock=socket(AF_INET, SOCK_STREAM, 0);
//    if(sock == -1){
//        printf("socket error\n");
//        exit(1);
//    }
//
//    memset(&serv_addr,0,sizeof(serv_addr));
//    serv_addr.sin_family=AF_INET;
//    serv_addr.sin_addr.s_addr = inet_addr(argv[1]);
//    serv_addr.sin_port = htons(atoi(argv[2]));
//    if(connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) == -1) {
//        printf("connect error\n");
//        exit(1);
//    }

    //연결 완료


    // WebCam 설정
    VideoCapture cap(0);

    // WebCam 해상도 설정
    //cap.set(CV_CAP_PROP_FRAME_WIDTH, 1280);
    //cap.set(CV_CAP_PROP_FRAME_HEIGHT, 720);
    cv::VideoWriter writer;
    // .jpg 파일 이름 설정
    int idx = 0;
    char buff[256];
    const char* pipe = "autovideosrc  ! videoscale ! video/x-raw, width=640, height=480  ! videoconvert ! x264enc ! queue ! rtph264pay config-interval=1 pt=96 ! udpsink host=127.0.0.1 port=9777 auto-multicast=true";
    
    writer.open(pipe ,CAP_GSTREAMER, 0, (double)30, cv::Size(640, 480), true);
    
    if (!writer.isOpened()) {
        printf("=ERR= can't create writer\n");
        return -1;
    }



    // WebCam 비활성화 상태일 경우 return
    if (!cap.isOpened())
    {
    printf("Can't open the WebCam\n");
    return -1;
    }

    cv::Mat frame;
    cv::Mat re_frame;

    while (1)
    {
        cap.read(frame);
        //imshow("WebCam Frame Capture", frame);

        // resizing frame 224 * 224
        //resize(frame, re_frame, Size(224, 224), 0, 0, INTER_LINEAR);

        // re_frame(224*224) 저장 (경로 : C:\WebCam\)
        //sprintf_s(buff, "C:\\WebCam\\img_%06d.jpg", idx);
        writer << frame;


//        file = fopen("12341234.jpg", "rb"); // const char* 만 가능
//        fseek(file,0,SEEK_END);
//        fsize = ftell(file);
//        fseek(file, 0, SEEK_SET);
//        fsize2 = htonl(fsize);
//        fsize2 = sizeof(re_frame);
//        ::send(sock, re_frame, fsize2,0);
//
//        while(nsize != fsize) {
//            fpsize = fread(file_buf, 1, 256, file);
//            nsize = nsize + fpsize;
//            send(sock, file_buf, fpsize, 0);
//        }
        //imwrite(buff, re_frame);

        idx++;
        if (idx == 999999)
            idx = 0;

        // WebCam 종료
        if (waitKey(1) == 27)
            break;
    }
    //close(sock);
    return 0;
}
//#include <iostream>
//#include <opencv2/core/core.hpp>
//#include <opencv2/highgui/highgui.hpp>
//
//
//using namespace std;
//using namespace cv;
//
//int main() {
//    Mat img = imread("lena.png");
//
//    if (img.empty()) {
//        printf("Image read failed");
//        exit(-1);
//    }
//
//    imshow("image", img);
//    waitKey(0);
//    return 0;
//}