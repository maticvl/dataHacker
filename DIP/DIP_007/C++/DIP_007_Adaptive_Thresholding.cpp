#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Loading the actual image
    Mat image, gray;
    Mat thresh1, thresh2;

    image=imread("daenerys.jpg", IMREAD_COLOR);
    cv::imshow("Original image", image);
    cv::waitKey();

    // Edge cases
    if(image.empty()){
    	cout << "Error loading image" << endl;
    	return -1;
    }

    // converting the color image into grayscale
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // ADAPTIVE_THRESH_MEAN_C - Threshold value is the mean of neighbourhood area.
    // ADAPTIVE_THRESH_GAUSSIAN_C - Threshold value is the weighted sum of neighbourhood
    // values where weights are a Gaussian window.
    // Block Size - It decides the size of neighbourhood area.
    // C - It is just a constant which is subtracted from the mean or weighted mean calculated.

    adaptiveThreshold(gray, thresh1, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 11, 2);
    adaptiveThreshold(gray, thresh2, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 11, 2);

    // Displaying the result
    cv::imshow("Adaptive Mean Thresholding", thresh1);
    cv::imshow("Adaptive Gaussian Thresholding", thresh2);

    cv::waitKey(0);
    return 0;
}
