#include <iostream>
#include <opencv2/opencv.hpp>
 
 
using namespace std;
using namespace cv;
 
int main() {
     
    cv::Mat image = imread("dragon.jpg", IMREAD_GRAYSCALE);
    cv::Mat processed_image;
     
    // we create a simple blur filter or a mean filter
    // all coefficients of this filter are the same
    // and this filter is also normalized.
     
     
    cv::imshow("Original image", image);
    cv::blur(image, processed_image, Size(3,3) );
    cv::waitKey();
     
    cv::imshow("Blur filter applied of size 3", processed_image);
    cv::waitKey();
     
     
    // Here we create an image of all zeros.
    // Only one pixel will be 1.
    // In this example we will generate a very small image so that we can
    // better visualize the filtering effect with such an image.
     
    cv::Mat image_impulse = cv::Mat::zeros(31, 31, CV_8UC1);
    image_impulse.at<uchar>(16,16) = 255;
     
     
     
    cv::imshow("Impulse image", image_impulse);
    cv::waitKey();
     
    cv::Mat image_impulse_processed;
     
 
    cv::blur(image_impulse, image_impulse_processed, Size(3,3));
    cv::imshow("Impulse image", image_impulse_processed);
    cv::waitKey();
     
    // this will produce a small square of size 3x3 in the center
    // Notice that, since the filter is normalized,
    // if we increase the size of the filter,
    // the intensity values of the square in the output image will be more lower. \
    // Hence, more challenging to be detected.
     
     
    cv::blur(image_impulse, image_impulse_processed, Size(7,7));
    cv::imshow("Impulse image", image_impulse_processed);
    cv::waitKey();
     
    // Gaussian filter
     
    // First we will just apply a Gaussian filter on the image
    // this will also create a blurring or smoothing effect..
    // Try visually to notice the difference as compared with the mean/box/blur filter.
     
     
    cv::Mat image_gaussian_processed;
    cv::GaussianBlur(image, image_gaussian_processed, Size(3,3), 1);
    cv::imshow("Gaussian processed", image_gaussian_processed);
    cv::waitKey();
     
    cv::GaussianBlur(image, image_gaussian_processed, Size(7,7), 1);
    cv::imshow("Gaussian processed", image_gaussian_processed);
    cv::waitKey();
     
    cv::Mat image_impulse_gaussian_processed;
    cv::GaussianBlur(image_impulse, image_impulse_gaussian_processed, Size(3,3), 1);
    cv::imshow("Gaussian processed - impulse image", image_impulse_gaussian_processed);
    cv::waitKey();
     
    cv::GaussianBlur(image_impulse, image_impulse_gaussian_processed, Size(7,7), 1);
    // here we have just multiplied an image to obtain a better visualization
    // as the pixel values will be too dark.
    image_impulse_gaussian_processed = image_impulse_gaussian_processed * 10;
    cv::imshow("Gaussian processed - impulse image", image_impulse_gaussian_processed);
    cv::waitKey();
     
     
    // here we will just add a random Gaussian noise to our original image
     
    cv::Mat noise_Gaussian = cv::Mat::zeros(image.rows, image.cols, CV_8UC1);
     
    // here a value of 64 is specified for a noise mean
    // and 32 is specified for the standard deviation
     
    cv::randn(noise_Gaussian, 64, 32);
     
    cv::Mat noisy_image, noisy_image1;
     
    noisy_image = image + noise_Gaussian;
    cv::imshow("Gaussian noise added - severe", noisy_image);
    cv::waitKey();
     
    //adding a very mild noise
    cv::randn(noise_Gaussian, 64, 8);
    noisy_image1 = image + noise_Gaussian;
    cv::imshow("Gaussian noise added - mild", noisy_image1);
    cv::waitKey();
 
    // Let's now apply a Gaussian filter to this.
    // This may be confusing for beginners.
    // We have one Gaussian distribution to create a noise
    // and other Gaussian function to create a filter, sometimes also called a kernel.
    // They should be treated completely independently.
 
    cv::Mat filtered_image;
    cv::GaussianBlur(noisy_image, filtered_image, Size(3,3), 3);
    cv::imshow("Gaussian noise severe - filtered", filtered_image);
    cv::waitKey();
     
    cv::GaussianBlur(noisy_image1, filtered_image, Size(7,7), 3);
    cv::imshow("Gaussian noise mild - filtered", filtered_image);
    cv::waitKey();
     
 
    return 0;
}
