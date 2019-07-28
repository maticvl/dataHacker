#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Loading the actual image
    Mat image, gray;
    Mat thresh1, thresh2, thresh3, thresh4, thresh5;

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

    // First type of Simple Thresholding is Binary Thresholding
    // After thresholding the image with this type of operator, we will
    // have image with only two values, 0 and 255.
    threshold( gray, thresh1, 127, 255, THRESH_BINARY );

    // Inverse binary thresholding is just the opposite of binary thresholding.
    threshold( gray, thresh2, 127, 255, THRESH_BINARY_INV );

    // Truncate Thresholding is type of thresholding where pixel
    // is set to the threshold value if it exceeds that value.
    // Othervise, it stays the same.
    threshold( gray, thresh3, 127, 255, THRESH_TRUNC );

    // Threshold to Zero is type of thresholding where pixel value stays the same
    // if it is greater than the threshold. Otherwise it is set to zero.
    threshold( gray, thresh4, 127, 255, THRESH_TOZERO );

    // Inverted Threshold to Zero is the opposite of the last one.
    // Pixel value is set to zero if it is greater than the threshold.
    // Otherwise it stays the same.
    threshold( gray, thresh5, 127, 255, THRESH_TOZERO_INV );
    // Displaying the result
    cv::imshow("THRESH_BINARY", thresh1);
    cv::imshow("THRESH_BINARY_INV", thresh2);
    cv::imshow("THRESH_TRUNC", thresh3);
    cv::imshow("THRESH_TOZERO", thresh4);
    cv::imshow("THRESH_TOZERO_INV", thresh5);

    cv::waitKey(0);
    return 0;
}
