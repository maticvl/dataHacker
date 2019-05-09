#include <opencv2/opencv.hpp>
  
using namespace std;
using namespace cv;
 
 
int main()
{
    // loading images
    Mat image = imread("sophie_turner.jpg",1);
    Mat logo = imread("datahacker.png",1);
 
    // initialization
    char file_name[100];
 
    // checking shapes
    cout << "Width : " << image.cols << endl;
    cout << "Height : " << image.rows << endl;
 
    cout << "Width : " << logo.cols << endl;
    cout << "Height : " << logo.rows << endl;
 
    // our starting coordinates
    int x = image.cols-logo.cols;
    int y = image.rows-logo.rows;
 
    // our image region of interest
    Mat imageROI = image(cv::Rect(x,y,logo.cols,logo.rows));
     
    // add the logo onto the image
    addWeighted(imageROI,1,logo,1,0.,imageROI);
     
    namedWindow("output",CV_WINDOW_AUTOSIZE);
    cv::imshow("output",image);
    cv::waitKey(0); // wait for a key pressed
    cv::destroyAllWindows();
 
    // save image
    sprintf(file_name, "added_logo.jpg");
    imwrite(file_name, image);
 
    cv::destroyAllWindows();
}
