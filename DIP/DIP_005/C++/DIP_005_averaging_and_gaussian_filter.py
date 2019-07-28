import cv2
import numpy as np

image = cv2.imread('dragon.jpg',0)

# we create a simple blur filter or a mean filter
# all coefficients of this filter are the same and this
# filter is also normalized.

cv2.imshow('Original image',image)
cv2.waitKey()

processed_image = cv2.blur(image,(5,5))

cv2.imshow('Blur filter applied of size 5',processed_image)
cv2.waitKey()

# Here we can create an image of all zeros.
# Only one pixel will be 1.
# In this example we will generate a very small image so that we can better
# visualize the filtering effect with such an image.

image_impulse = np.zeros((31,31),dtype='uint8')
image_impulse[16,16] = 255

cv2.imshow('Impulse image',image_impulse)
cv2.waitKey()

image_impulse_processed = cv2.blur(image_impulse,(3,3))

cv2.imshow('Impulse image',image_impulse_processed)
cv2.waitKey()

# This will produce a small square of size 3x3 in the center
# Notice that, since the filter is normalized, if we increase the size of the filter,
# the intesity values of the square in the ouput image will be more lower.
# Hence, more challenging to be detected.

image_impulse_processed = cv2.blur(image_impulse,(7,7))

cv2.imshow('Impulse image',image_impulse_processed)
cv2.waitKey()


# First we will just apply a Gaussian filter on the image
# This will also create a blurring or smoothing effect.
# Try visually to notice the difference as compared with the mean/box/blur filter.

image_gaussian_processed = cv2.GaussianBlur(image,(3,3),1)

cv2.imshow('Gaussian processed',image_gaussian_processed)
cv2.waitKey()

image_gaussian_processed = cv2.GaussianBlur(image,(7,7),1)

cv2.imshow('Gaussian processed',image_gaussian_processed)
cv2.waitKey()


image_impulse_gaussian_processed = cv2.GaussianBlur(image_impulse,(3,3),1)

cv2.imshow('Gaussian processed - impulse image',image_impulse_gaussian_processed)
cv2.waitKey()

image_impulse_gaussian_processed = cv2.GaussianBlur(image_impulse,(3,3),1)
# Here we have just multiplied an image to obtain a better visualization
# As the pixel  values will be too dark,

image_impulse_gaussian_processed = image_impulse_gaussian_processed * 10

cv2.imshow('Gaussian processed - impulse image',image_impulse_gaussian_processed)
cv2.waitKey()

# Here we will just add a random Gaussian noise to our original image

noise_Gaussian = np.zeros((image.shape[0], image.shape[1]), dtype='uint8');

# Here a value of 64 is specified for a noise mean
# and 32 is specified for the standard deviation

cv2.randn(noise_Gaussian, 64, 32)

noisy_image = cv2.add(image, noise_Gaussian) 
cv2.imshow("Gaussian noise added - severe", noisy_image)
cv2.waitKey()

# Adding a very mild noise
cv2.randn(noise_Gaussian, 64, 8)
noisy_image1 = cv2.add(image, noise_Gaussian) 
cv2.imshow("Gaussian noise added - mild", noisy_image1)
cv2.waitKey()


# Let's now apply a Gaussian filter to this.
# This may be confusing for beginners.
# We have one Gaussian distribution to create a noise
# and other Gaussian function to create a filter, sometimes also called a kernel.
# They should be treated completely independently.

filtered_image = cv2.GaussianBlur(noisy_image, (3,3), 3)
cv2.imshow("Gaussian noise severe - filtered", filtered_image)
cv2.waitKey()

filtered_image = cv2.GaussianBlur(noisy_image1, (7,7), 3)
cv2.imshow("Gaussian noise mild - filtered", filtered_image)
cv2.waitKey()
