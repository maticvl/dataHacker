import cv2

# Read the image and convert it to a grayscale
image = cv2.imread("03.jpg")
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Detect corner
output = cv2.cornerHarris(gray,2,3,0.04)

# Results are marked through the dilated corners
# cv2.dilate dilates an image by using a specific structuring element.
# It is used to increases the object area and to emphasize features
output = cv2.dilate(output,None)

# Threshold and place red dots at detection points
image[output>0.1*output.max()]=[0,0,255]

cv2.imshow('Output',image)
cv2.waitKey(0)
cv2.destroyAllWindows()