import cv2

# read the image as a grayscale
image = cv2.imread('daenerys.jpg',0)

# cv2.ADAPTIVE_THRESH_MEAN_C - Threshold value is the mean of neighbourhood area.
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C - Threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
# Block Size - It decides the size of neighbourhood area.
# C - It is just a constant which is subtracted from the mean or weighted mean calculated.

th1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("Adaptive Mean Thresholding", th1)
cv2.imshow("Adaptive Gaussian Thresholding", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()
