#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() 
{
    
	// Noise generation.
    // Let's start with a basic method to generate random number using OpenCV.
    // For this we will use a cv::RNG method
    // the code below illustrates how we can obtain 2 random numbers from uniform distribution
    
    // this returns the random number generator
    cv::RNG rng = theRNG();
    // two random numbers will be generated
    // from the uniform distribution [0,1].
    float a = rng.uniform(0.f, 1.f); float b = rng.uniform(0.f, 1.f);
    // printing two random numbers
    std::cout << "a:" << a << std::endl << "b:" << b <<  std::endl;
    
    // in the similar manner we can get two random numbers from a normal distribution
    
    // Here we can just specify the sigma value (we have use a value 1)
    // the distribution will be zero centered.
    
    float a_g = rng.gaussian(1);
    
    std::cout << a_g << std::endl ;

	// Another way to generate the random values form the same distribution is to use
    // functions randu and randn
    
    cv::Mat image = cv::imread("a11.jpg", IMREAD_GRAYSCALE);
    
    // Let's first create a zero image with the same dimensions of the loaded image
    
    cv::Mat gaussian_noise = cv::Mat::zeros (image.rows, image.cols, CV_8UC1);
    
    cv::imshow("All zero values", gaussian_noise);
    cv::waitKey();
    
    // now, we can set the pixel values as a Gaussian noise
    // we have set a mean value to 128 and a standard deviation to 20
    cv::randn(gaussian_noise, 128, 20);
    
    // Let's plot this image and see how it looks like
    cv::imshow("Gaussian noise", gaussian_noise);
    cv::waitKey();

    cv::imwrite("Gaussian random noise.jpg", gaussian_noise);
	
	    
	// In a similar manner we can create an image whose pixel values have
    // random values drawn from an uniform distribution
    
    cv::Mat uniform_noise = cv::Mat::zeros (image.rows, image.cols, CV_8UC1);
    
    cv::randu(uniform_noise, 0, 255);
    cv::imshow("Uniform random noise", uniform_noise );
    cv::waitKey();
    cv::imwrite("Uniform random noise.jpg", uniform_noise);
	
	
    cv::Mat impulse_noise = uniform_noise.clone();
    
    
    // here a number 250 is defined as a threshold value
    // Obviously, if we want to increase a number of white pixels
    // we will need to decrease it.
    // Otherwise, we can increase it and in that way we will suppress the
    // number of white pixles.
    
    cv::threshold(uniform_noise, impulse_noise, 250, 255, CV_8UC1);
    
    cv::imshow("Impulse_noise", impulse_noise);
    cv::waitKey();
    cv::imwrite("Impulse_noise.jpg", impulse_noise);
	
	// Adding noise to images
    cv::Mat noisy_image1=image.clone();
    // note that we acan simply sum to Mat objects, that is, two images.
    // in order not to degrade the image quality too much
    // we will multipliy the gaussian_noise with 0.5.
    // in this way the noise of effect will be reduced
    noisy_image1 = image + gaussian_noise*0.5;
    
    cv::imshow("Noisy_image - Gaussian noise", noisy_image1);
    cv::waitKey();
    
    cv::Mat noisy_image2=image.clone();
    // similarly for a uniform noise, we will use even a lower factor of 0.2
    
    noisy_image2 = image + uniform_noise*0.2;
    
    cv::imshow("Noisy_image - Gaussian noise", noisy_image2);
    cv::waitKey();
    
    // Median filtering
    // Applying a simple median filter.
    // There are, of course, as we will see, more advanced filters.
    // However, not that even a simple median filter can do,
    // rather effective job.
    // This is true especially, for ? Well, you guess it.
    
    cv::medianBlur(noisy_image, noisy_image, 3);
    cv::imshow("Impulse random noise removed", noisy_image);
    cv::waitKey();

    cv::medianBlur(noisy_image1, noisy_image1, 3);
    cv::imshow("Gaussian random noise removed", noisy_image1);
    cv::waitKey();

    cv::medianBlur(noisy_image2, noisy_image2, 3);
    cv::imshow("Uniform random noise removed", noisy_image2);
    cv::waitKey();

