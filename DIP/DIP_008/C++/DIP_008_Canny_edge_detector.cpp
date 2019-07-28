#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Loading the actual image
    Mat image, gray, edges;

    image=imread("daenerys.jpg", IMREAD_COLOR);

    // Edge cases
    if(image.empty()){
    	cout << "Error loading image" << endl;
    	return -1;
    }

    // converting the color image into grayscale
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // Detect edges with Canny Edge Detector
    // First argument is the input image.
    // Second argument is the output image.
    // Third and fourth arguments are the minVal and maxVal.
    // Fifth argument is the size of Sobel kernel used for find image gradients (aperture_size).
    // Last argument is L2gradient.
    Canny(image, edges, 100, 200, 3);

    // Displaying the result
    cv::imshow("Original image", image);
    cv::imshow("Canny Edge Detector", edges);

    cv::waitKey(0);
    return 0;
}