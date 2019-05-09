#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main() {
    
    cv::Mat img;
    
    // using the following argument we will load a preprocessed image
    // in this case RGB image will be converted into a gray scale image
    img = cv::imread("sophie_turner.jpg", IMREAD_GRAYSCALE) ;
    
    // changing some grayscale pixel values
    for (int k = 0; k<50; k++) {
        
        for(int j=0;j<img.rows;j++){

            for (int i=0;i<img.cols;i++){
            
                img.at<uchar>(j,i) = img.at<uchar>(j,i) * 0.97 ; //darker
            }

        }

        cv::imshow("Updated",img);
        cv::waitKey(40);
    }
    return 0;    
}
