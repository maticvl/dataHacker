#include <opencv2/opencv.hpp>
  
using namespace cv;
using namespace std;
 
int main() {
 
    // file name
    char file_name[100];
 
    // read the image and logo
    cv::Mat image=  cv::imread("sophie_turner.jpg", 1); 
    cv::Mat logo=  cv::imread("datahacker.png", 1); 
 
    // our starting coordinates
    int x = image.cols-logo.cols;
    int y = image.rows-logo.rows;
 
    // define image ROI at image bottom-right
    Mat imageROI= image(cv::Rect(x,y, logo.cols, logo.rows));
 
    // here we inverted the color (so all black are now white and all white are now black)
    cv::Mat invSrc =  cv::Scalar::all(255) - logo;
 
    // use the logo as a mask (must be gray-level)
    cv::Mat mask(invSrc);
 
    // insert by copying only at locations of non-zero mask
    invSrc.copyTo(imageROI, mask);
 
    cv::imshow("Image", image); // show the image
    cv::namedWindow("Image"); 
    cv::waitKey(0); // wait for a key pressed
    cv::destroyAllWindows();
 
    // save image
    sprintf(file_name, "added_transperant_logo.jpg");
    imwrite(file_name, image);
 
    return 0;
}
