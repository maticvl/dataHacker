import cv2
import numpy as np

image = cv2.imread('dragon.jpg',0)
cv2.imshow('Original image',image)
cv2.waitKey()

# We have already explained linear filters for horizontal and vertical edge detection

# this is how we can create a horizontal edge detector.
# cv2.Sobel(src_gray, depth, x_order, y_order)
# src_gray: The input image.
# depth: The depth of the output image.
# x_order: The order of the derivative in x direction.
# y_order: The order of the derivative in y direction.
# To calculate the gradient in x direction we use: x_order= 1 and y_order= 0.
# To calculate the gradient in x direction we use: x_order= 0 and y_order= 1.
image_X = cv2.Sobel(image, cv2.CV_8UC1, 1, 0)

cv2.imshow("Sobel image", image_X)
cv2.waitKey()

image_Y = cv2.Sobel(image, cv2.CV_8UC1, 0, 1)
cv2.imshow("Sobel image", image_Y)
cv2.waitKey()

# When we combine the horizontal and vertical edge detector together
sobel = cv2.add(image_X, image_Y)
cv2.imshow("Sobel - L1 norm", sobel)
cv2.waitKey()

(_, sobmin, _, sobmax) = cv2.minMaxLoc(sobel)
# this idea is inspired from the book
# "Robert Laganiere Learning OpenCV 3:: computer vision"
# what it actually does, makes the non-edges to white values
# and edges to dark values, so that it is more common for our visual interpretation.
# this is done according to formula
# sobelImage = - alpha * sobel +  255;

#sobel.convertTo(sobelImage, CV_8UC1, -255./sobmax, 255);

sobelImage = np.int16(sobel)     # convert to signed 16 bit integer to allow overflow
sobelImage = np.clip(sobelImage, -255./sobmax[0], 255) # force all values to be between -255./sobmax and 255

# after clip img2 is effectively unsigned 8 bit, but make it explicit:
sobelImage = np.uint8(sobelImage)

cv2.imshow("Edges with a sobel detector", sobelImage)
cv2.waitKey()

(_, sobmin, _, sobmax) = cv2.minMaxLoc(sobelImage)
# image_Laplacian = image_Laplacian / max_value * 255

image_Sobel_thresholded = cv2.threshold(sobelImage, 20, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Laplacian", image_Sobel_thresholded[1])
cv2.waitKey()

# Also, very popular filter for edge detection is Laplacian operator
# It calculates differences in both x and y direction and then sums their amplitudes.

# here we will apply low pass filtering in order to better detect edges
# try to uncomment this line and the result will be much poorer.
image = cv2.GaussianBlur(image,(5,5),1)

image_Laplacian = cv2.Laplacian(image, cv2.CV_8UC1)

cv2.imshow("The Laplacian", image_Laplacian)
cv2.waitKey()

(_, min_value1, _, max_value1) = cv2.minMaxLoc(image_Laplacian)
#image_Laplacian = image_Laplacian / max_value * 255;

image_Laplacian_thresholded = cv2.threshold(image_Laplacian,70, 220, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Laplacian", image_Laplacian_thresholded[1])
cv2.waitKey()
