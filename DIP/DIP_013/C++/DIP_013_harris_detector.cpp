#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    Mat image, gray;
    Mat output, output_norm, output_norm_scaled;

    // Loading the actual image
    image = imread("03.jpg", IMREAD_COLOR);

    // Edge cases
    if(image.empty()){
    	cout << "Error loading image" << endl;
    	return -1;
    }
    cv::imshow("Original image", image);
    cv::waitKey();

    // Converting the color image into grayscale
    cvtColor(image, gray, CV_BGR2GRAY);

    // Detecting corners
    output = Mat::zeros(image.size(), CV_32FC1);
    cornerHarris(gray, output, 2, 3, 0.04);

    // Normalizing
    normalize(output, output_norm, 0, 255, NORM_MINMAX, CV_32FC1, Mat());
    convertScaleAbs(output_norm, output_norm_scaled);

    // Drawing a circle around corners
    for(int j = 0; j < output_norm.rows ; j++){
        for(int i = 0; i < output_norm.cols; i++){
            if((int) output_norm.at<float>(j,i) > 100){
               circle(image, Point(i,j), 2,  Scalar(0,0,255), 2, 8, 0 );
            }
        }
    }

    // Displaying the result
    cv::imshow("Output", image);
    cv::waitKey();
    cv::imwrite("output.jpg", image);
    return 0;
}