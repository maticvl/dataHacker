#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main() {
    
    cv::Mat img;
    
    // using the following argument we will load a preprocessed image
    // in this case RGB image will be converted into a gray scale image
    img = cv::imread("sophie_turner.jpg", IMREAD_GRAYSCALE);
    
    // changing some grayscale pixel values
    for (int k = 0; k<50; k++) {

        for(int j=0;j<img.rows;j++){

            for (int i=0;i<img.cols;i++){

                // prevents that multiplication with 1.03, creates a number larger than 255
                if (img.at<uchar>(j,i) < (255-30)){ 

                    img.at<uchar>(j,i) = img.at<uchar>(j,i) * 1.03; //white       
                
                }
            }   
        }
        cv::imshow("Updated",img);
        cv::waitKey(40);
    }

   return 0;    
}
