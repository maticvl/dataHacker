import cv2

# read the image as a grayscale
image = cv2.imread('daenerys.jpg',0)

# Detect edges with Canny Edge Detector
# First argument is the input image.
# Second and third arguments are the minVal and maxVal.
# Third argument is the size of Sobel kernel used for find image gradients (aperture_size).
# Last argument is L2gradient.
edges = cv2.Canny(image,100,200,3)

cv2.imshow("Original image", image)
cv2.imshow("Canny Edge Detector", edges)
cv2.waitKey(0)
cv2.destroyAllWindows();