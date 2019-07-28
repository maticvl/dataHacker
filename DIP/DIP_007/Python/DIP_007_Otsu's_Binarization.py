import cv2

# read the image as a grayscale
image = cv2.imread('daenerys.jpg',0)

# Otsu's thresholding
ret1,th1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding with Gaussian filtering
blurred = cv2.GaussianBlur(image,(5,5),0)
ret2,th2 = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Otsu's thresholding", th1)
cv2.imshow("Otsu's thresholding with Gaussian filtering", th2)
cv2.waitKey(0)
cv2.destroyAllWindows();
