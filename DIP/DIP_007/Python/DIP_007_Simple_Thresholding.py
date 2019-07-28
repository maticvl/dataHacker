import cv2

# read the image as a grayscale
image = cv2.imread('daenerys.jpg',0)

# First type of Simple Thresholding is Binary Thresholding
# After thresholding the image with this type of operator, we will
# have image with only two values, 0 and 255.
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

# Inverse binary thresholding is just the opposite of binary thresholding.
ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)

# Truncate Thresholding is type of thresholding where pixel
# is set to the threshold value if it exceeds that value.
# Othervise, it stays the same.
ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)

# Threshold to Zero is type of thresholding where pixel value stays the same
# if it is greater than the threshold. Otherwise it is set to zero.
ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)

# Inverted Threshold to Zero is the opposite of the last one.
# Pixel value is set to zero if it is greater than the threshold.
# Otherwise it stays the same.
ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("THRESH_BINARY", thresh1)
cv2.imshow("THRESH_BINARY_INV", thresh2)
cv2.imshow("THRESH_TRUNC", thresh3)
cv2.imshow("THRESH_TOZERO", thresh4)
cv2.imshow("THRESH_TOZERO_INV", thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows();
