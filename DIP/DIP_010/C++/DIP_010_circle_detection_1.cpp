#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Loading the actual image
    Mat image, gray;
    image=imread("CirclesDetection.jpg", IMREAD_COLOR);
    cv::imshow("Original image", image);
    cv::waitKey();

    // Edge cases
    if(image.empty()){
        cout << "Error loading image" << endl;
        return -1;
    }

    // converting the color image into grayscale
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // Smoothing the image to get rid of noise, so no false detections
    // Here we used a 11x11 filter
    medianBlur( gray, gray, 11);
    cv::imshow("Blurred_image", gray);
    //cv::imwrite("Blurred_image.jpg", gray);
    cv::waitKey();

    // Store the detected circles in a 3d-vector
    vector<Vec3f> circles;
    
    // Apply hough transform
    HoughCircles(gray, circles, HOUGH_GRADIENT, 1,
                 100, // detect circle with different distance
                 100, 100,
                 0,200);

    // Draw the detected circles
    for( size_t i = 0; i < circles.size(); i++ )
    {
         Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
         int radius = cvRound(circles[i][2]);
         // Draw the center point of the circle
         circle( image, center, 3, Scalar(0,255,0), -1, 8, 0 );
         // Draw the circle shape
         circle( image, center, radius, Scalar(0,255,0), 3, 8, 0 );
    }

    // Displaying the result
    cv::imshow("circles", image );
    cv::imwrite("output.jpg", image);
    cv::waitKey(0);
    return 0;
}
