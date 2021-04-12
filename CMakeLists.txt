cmake_minimum_required (VERSION 2.8) 
 
set(CMAKE_MODULE_PATH "/usr/local/lib/cmake/${CMAKE_MODULE_PATH}") 
find_package(raspicam REQUIRED)
find_package(OpenCV)
 
add_executable (raspicamview raspicamview.cpp)  
target_link_libraries (raspicamview ${raspicam_CV_LIBS})