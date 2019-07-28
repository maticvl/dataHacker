# import opencv library
import cv2
import numpy as np

# read the image
image = cv2.imread('sophie_turner.jpg')
logo  = cv2.imread('datahacker.png')

(hi, wi) = image.shape[:2]
(hw, ww) = logo.shape[:2]

overlay = np.zeros((hi, wi, 3), dtype="uint8")
overlay[hi - hw:hi, wi - ww:wi] = logo

# add the logo onto the image
# cv2.addWeighted calculates the weighted sum of two arrays
output = image.copy()
cv2.addWeighted(image, 1, overlay, 1, 0, output)

cv2.imwrite("output.jpg", output)
cv2.imshow("output", output)
cv2.waitKey()
cv2.destroyAllWindows()