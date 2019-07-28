import cv2
import numpy as np

# read the image
original = cv2.imread('003.jpg')

for k in range(0,50):
    original[:,:,0] = original[:,:,0] / 1.03
    original[:,:,1] = original[:,:,1] * 1.02
    original[:,:,2] = original[:,:,2] * 0
      
    # show the results
    cv2.imshow('Updated',original)
    cv2.waitKey(40)
cv2.destroyAllWindows()