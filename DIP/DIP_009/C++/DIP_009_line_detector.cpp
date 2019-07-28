#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Declare the output variables
    Mat edgeImage, orginalImageWithHoughLines;
    
    // Loads an image
    Mat image = imread( "road.jpg", IMREAD_GRAYSCALE);

    // Check if image is loaded fine
    if(image.empty()){
        printf(" Error opening imagen");
       return -1;
    }

    // Apply the Guassian Blur filter to smooth the image
    cv::Mat image_gaussian_processed;
    cv::GaussianBlur(image, image_gaussian_processed, Size(5,5), 1);

    // Edge detection
    Canny(image_gaussian_processed, edgeImage, 50, 120, 3);

    // Copy loaded image to the initial image so that will display the results in BGR
    cvtColor(image, orginalImageWithHoughLines, COLOR_GRAY2BGR);

    // Declaring some constants for the parameters
    int dis_reso = 1;
    double theta = CV_PI/180;
    int threshold = 170;

    // Standard Hough Line Transform
    vector<Vec2f> lines; // will hold the results of the detection
    HoughLines(edgeImage, lines, dis_reso, theta, threshold, 0, 0); // runs the actual detection

    // Draw the lines
    for( size_t i = 0; i < lines.size(); i++ )
    {
        float rho = lines[i][0], theta = lines[i][1];
        Point pt1, pt2;
        double a = cos(theta), b = sin(theta);
        double x0 = a*rho, y0 = b*rho;
        pt1.x = cvRound(x0 + 1000*(-b));
        pt1.y = cvRound(y0 + 1000*(a));
        pt2.x = cvRound(x0 - 1000*(-b));
        pt2.y = cvRound(y0 - 1000*(a));
        line( orginalImageWithHoughLines, pt1, pt2, Scalar(0,255,00), 3, LINE_AA);
    }

    //cvtColor(image, image, COLOR_GRAY2BGR);
    //cvtColor(orginalImageWithHoughLines, orginalImageWithHoughLines, COLOR_GRAY2BGR);

    // Show results
    cv::imshow("Original image", image);
    cv::imshow("Detected Lines (in Green) - Standard Hough Line Transform", orginalImageWithHoughLines);
    // Wait and Exit
    waitKey(0);

    return 0;
}