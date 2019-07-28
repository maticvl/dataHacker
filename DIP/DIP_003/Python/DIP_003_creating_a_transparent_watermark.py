import cv2
import numpy as np

# read the image and logo
image = cv2.imread('003.jpg', cv2.IMREAD_UNCHANGED)
logo  = cv2.imread('datahacker.png', cv2.IMREAD_UNCHANGED)

# here we inverted the color (so all black are now white and all white are now black)
logo = cv2.bitwise_not(logo) 

# extracted the width and height of the image
(hl, wl) = logo.shape[:2] 
(hi, wi) = image.shape[:2]

image = np.dstack([image, np.ones((hi, wi), dtype="uint8") * 255])

overlay = np.zeros((hi, wi, 4), dtype="uint8")
overlay[hi - hl: hi, wi - wl:wi] = logo

# Performing transistion from one color onto another
cv2.addWeighted(overlay, 1, image, 1.0, 0, image)

# save the image
cv2.imwrite("added_transperant_logo.jpg", image)
cv2.imshow("added_transperant_logo", image)
cv2.waitKey()
cv2.destroyAllWindows()