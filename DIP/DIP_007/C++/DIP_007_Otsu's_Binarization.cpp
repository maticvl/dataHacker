#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Loading the actual image
    Mat image, gray, blurred;
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

    // Otsu's thresholding
    threshold(gray, thresh1, 0, 255, THRESH_BINARY+THRESH_OTSU);

    // Otsu's thresholding with Gaussian filtering
    GaussianBlur(gray, blurred, Size(5,5),0);
    threshold(blurred, thresh2, 0, 255, THRESH_BINARY+THRESH_OTSU);

    // Displaying the result
    cv::imshow("Otsu's thresholding", thresh1);
    cv::imshow("Otsu's thresholding with Gaussian filtering", thresh2);

    cv::waitKey(0);
    return 0;
}
