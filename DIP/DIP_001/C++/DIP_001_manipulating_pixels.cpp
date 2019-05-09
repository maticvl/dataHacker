#include <opencv2/opencv.hpp> //Include file for every supported OpenCV function. Hint: Slow to compile.

using namespace cv;  // optional 
using namespace std; 

int main ( int argc, char** argv  ) {
    
    // initialization
    cv::Mat image;
    int x=0, y=0;

    // place an image in the working folder
    image = cv::imread("sophie_turner.jpg", IMREAD_COLOR );

    // we will use this command to show an image.
    // the first argument is the title of the window, the second one is the loaded image (MAT format)
    cv::imshow("Window 1", image);

    // we wait for a key to be pressed, and then we exit.
    cv::waitKey(0);

// the following piece of code reads a single pixel value
    // then it prints it.

    // 3 channel image with BGR color (type 8UC3)
    // the values can be stored in "int" or in "uchar". Here int is 
    //used.
    cv::Vec3b intensity = image.at<Vec3b>(y, x);

    float blue = intensity.val[0];
    float green = intensity.val[1];
    float red = intensity.val[2];

    std::cout << "Blue:" << blue << std::endl;
    std::cout << "Green:" << green  << std::endl;
    std::cout << "Red:" << red << std::endl;

    // changing a single pixel color at the location (x,y)
    // get a pixel
    cv::Vec3b color = image.at<Vec3b>(Point(x,y));

    color[0]=0;
    color[1]=255;
    color[2]=0;
 
    // set a pixel back to the image
    image.at<Vec3b>(Point(x,y)) = color;

    cv::imshow("Changed one pixel value", image);
    waitKey(0);

    // change the part of the image into a certain color
   // this code snippet will loop over an upper-top rectangle, 
// it will access each pixel and change its value. 
// Following OpenCV's format BGR, we will get green pixels. 
// That is, a green rectangle in the upper top image.  

    for (x=0; x<100; x++) {

        for (y=0; y<100; y++ ){

        // get a pixel
        cv::Vec3b color = image.at<Vec3b>(Point(x,y));

        color[0]=0;
        color[1]=255;
        color[2] =0;

        // set a pixel back to the image
        image.at<Vec3b>(Point(x,y)) = color;
 
       }
    }

    cv::imshow("Changed a part of the image", image);
    waitKey(0);

    // Saving the image
    cv::imwrite( "new_image.jpg", image);

    return 0;
}