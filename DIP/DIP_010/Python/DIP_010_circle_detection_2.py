import numpy as np
import cv2

image = cv2.imread("CirclesDetection.jpg",0)
output = cv2.imread("CirclesDetection.jpg",1)
cv2.imshow("Original image", image)
cv2.waitKey()

blurred = cv2.GaussianBlur(image,(11,11),0)

cv2.imshow("Blurred image", blurred)
cv2.waitKey()

#Finds circles in a grayscale image using the Hough transform
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,
                             param1=100,param2=90,minRadius=0,maxRadius=200)

# cv2.HoughCircles function has a lot of parameters, so you can find more about it in documentation
# or you can use cv2.HoughCircles? in jupyter nootebook to get that 

# Check to see if there is any detection
if circles is not None:
    # If there are some detections, convert radius and x,y(center) coordinates to integer
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        # Draw the circle in the output image
        cv2.circle(output, (x, y), r, (0,255,0), 3)
        # Draw a rectangle(center) in the output image
        cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)

cv2.imshow("Detections",output)
cv2.imwrite("output.jpg",output)
cv2.waitKey()