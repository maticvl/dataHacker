#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{

    Mat image = cv::imread("dragon.jpg", IMREAD_GRAYSCALE);
    cv::imshow("Dragon", image);
    cv::waitKey();

    // we have already explained linear filters for horizontal and vertical edge detection
    // reference -->> CNN #002, CNN #003 posts.

    cv::Mat image_X;
    // this is how we can create a horizontal edge detector
    // Sobel(src_gray, dst, depth, x_order, y_order)
    // src_gray: The input image.
    // dst: The output image.
    // depth: The depth of the output image.
    // x_order: The order of the derivative in x direction.
    // y_order: The order of the derivative in y direction.
    // To calculate the gradient in x direction we use: x_order= 1 and y_order= 0.
    // To calculate the gradient in x direction we use: x_order= 0 and y_order= 1.
    cv::Sobel(image, image_X, CV_8UC1, 1, 0);
    cv::imshow("Sobel image", image_X);
    cv::waitKey();

    cv::Mat image_Y;
    // this is how we can create a vertical edge detector.
    cv::Sobel(image, image_Y, CV_8UC1, 0, 1);
    cv::imshow("Sobel image", image_Y);
    cv::waitKey();

    // When we combine the horizontal and vertical edge detector together
    cv::Mat sobel = image_X + image_Y;
    cv::imshow("Sobel - L1 norm", sobel);
    cv::waitKey();

    // this idea is inspired from the book
    // "Robert Laganiere Learning OpenCV 3:: computer vision"
    // what it actually does, makes the non-edges to white values
    // and edges to dark values, so that it is more common for our visual interpretation.
    // this is done according to formula
    // sobelImage = - alpha * sobel +  255;
    double sobmin, sobmax;
    cv::minMaxLoc(sobel, &sobmin, &sobmax);

    cv::Mat sobelImage;
    sobel.convertTo(sobelImage, CV_8UC1, -255./sobmax, 255);
    cv::imshow("Edges with a sobel detector", sobelImage);
    cv::waitKey();


    cv::Mat image_Sobel_thresholded;
    double max_value, min_value;
    cv::minMaxLoc(sobelImage, &min_value, &max_value);
    //image_Laplacian = image_Laplacian / max_value * 255;


    cv::threshold(sobelImage, image_Sobel_thresholded, 20, 255, cv::THRESH_BINARY);
    cv::imshow("Thresholded Sobel", image_Sobel_thresholded);
    cv::waitKey();
    // Also, very popular filter for edge detection is Laplacian operator
    // It calculates differences in both x and y direction and then sums their amplitudes.

    cv::Mat image_Laplacian;
    // here we will apply low pass filtering in order to better detect edges
    // try to uncomment this line and the result will be much poorer.
    cv::GaussianBlur(image, image, Size(5,5), 1);

    cv::Laplacian(image, image_Laplacian, CV_8UC1);
    cv::imshow("The Laplacian", image_Laplacian);
    cv::waitKey();

    cv::Mat image_Laplacian_thresholded;
    double max_value1, min_value1;
    cv::minMaxLoc(image_Laplacian, &min_value1, &max_value1);
    //image_Laplacian = image_Laplacian / max_value * 255;


    cv::threshold(sobel, image_Laplacian_thresholded, 70, 220, cv::THRESH_BINARY);
    cv::imshow("Thresholded Laplacian", image_Laplacian_thresholded);
    cv::waitKey();

    return 0;
}
