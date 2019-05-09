#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;
int main() {
    
    Mat original;
    
    original = cv::imread("sophie_turner.jpg", IMREAD_COLOR);
    
    // a loop that iteratively increases/decreases certain color channels
    // we create a fade-in/fade-out effect in color. 
    for (int k = 0; k<50; k++) {
    
        for (int r=0; r<original.rows; r++){
        
            for (int c=0; c< original.cols; c++){
            
                // in this way we can access the pixel values at (r, c) position
                // in this example we multiply these values with a constant 0.5f
                // note that it will still be saved as uint8_t type

                // hint: we are working with 8bit grayscale images.

                // original.at<uint8_t>(r, c) = original.at<uint8_t>(r, c)  * 0.5f;

                // have a look how we are going to process a color image.
                // we will use Vec3b
                // in this case we can treat a single position as a vector of 3 bytes (b)
                // try for yourself how changing some values produce different examples

                original.at<Vec3b>(r, c) [0]= original.at<Vec3b>(r, c)[0]  * 0.f;
                original.at<Vec3b>(r, c) [1]= original.at<Vec3b>(r, c)[1]  * 1.03f;
                original.at<Vec3b>(r, c) [2]= original.at<Vec3b>(r, c)[2]  / 1.02f;
            }
        }

        cv::imshow("Updated",original);
        cv::waitKey(40);
    }
    
    return 0;    
    
}
