import cv2
import numpy as np
import random

# The code below illustrates how we can obtain 2 random numbers from uniform distribution.
a = np.random.uniform(0,1)
b = np.random.uniform(0,1)

print(' a: ',a,'\n','b: ',b)

# In the similar manner we can get two random numbers from a normal distribution
a = np.random.normal(0,1)
b = np.random.normal(0,1)

# Let's first create a zero image with the same dimensions of the loaded image
image = cv2.imread('a11.jpg')

gaussian_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
cv2.imshow('All zero values',gaussian_noise)
cv2.waitKey()

# Now, we can set the pixel values as a Gaussian noise. We have set a mean value
# to 128 and a standard deviation to 20.
cv2.randn(gaussian_noise, 128, 20)

cv2.imshow('Gaussian noise',gaussian_noise)
cv2.waitKey()
cv2.imwrite("Gaussian random noise.jpg",gaussian_noise)

# In a similar manner we can create an image whose pixel values have random values
# drawn from an uniform distribution.
uniform_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)

cv2.randu(uniform_noise,0,255)
cv2.imshow('Uniform random noise',uniform_noise)
cv2.waitKey()
cv2.imwrite("Uniform random noise.jpg",uniform_noise)

# And third important type of noise will be a black and pepper.
# Here we will due to a bit simplar visualization represent only a noise that has white pixels.
# One approach to do so is to let's say simply take a "uniform_noise" image.
# Set a threshold rule, where we will convert all pixels larger than a threshold to white (255)
# and we will set the remaining to zero.
impulse_noise = uniform_noise.copy()
# Here a number 250 is defined as a threshold value.
# Obviously, if we want to increase a number of white pixels we will need to decrease it.
# Otherwise, we can increase it and in that way we will suppress the number of white pixels.
ret,impulse_noise = cv2.threshold(uniform_noise,250,255,cv2.THRESH_BINARY)

cv2.imshow('Impuls noise',impulse_noise)
cv2.waitKey()
cv2.imwrite("Impuls noise.jpg",impulse_noise)

image = cv2.imread('a11.jpg',cv2.IMREAD_GRAYSCALE)
gaussian_noise = (gaussian_noise*0.5).astype(np.uint8)
noisy_image1 = cv2.add(image,gaussian_noise)

cv2.imshow('Noisy image - Gaussian noise',noisy_image1)
cv2.waitKey()
cv2.imwrite("Noisy image1.jpg",noisy_image1)

uniform_noise = (uniform_noise*0.5).astype(np.uint8)
noisy_image2 = cv2.add(image,uniform_noise)

cv2.imshow('Noisy image - Uniform noise',noisy_image2)
cv2.waitKey()
cv2.imwrite("Noisy image2.jpg",noisy_image2)

impulse_noise = (impulse_noise*0.5).astype(np.uint8)
noisy_image3 = cv2.add(image,impulse_noise)

cv2.imshow('Noisy image - Impuls noise',noisy_image3)
cv2.waitKey()
cv2.imwrite("Noisy image3.jpg",noisy_image3)

# Applying a simple median filter.
# There are, of course, as we will see, more advanced filters.
# However, not that even a simple median filter can do, rather effective job.
# This is true especially, for ? Well, you guess it.
blurred1 = cv2.medianBlur(noisy_image1, 3)
cv2.imshow('Median filter - Gaussian noise',blurred1)
cv2.waitKey()
cv2.imwrite("Median filter - Gaussian noise.jpg",blurred1)

blurred2 = cv2.medianBlur(noisy_image2, 3)
cv2.imshow('Median filter - Uniform noise',blurred2)
cv2.waitKey()
cv2.imwrite("Median filter - Uniform noise.jpg",blurred2)

blurred3 = cv2.medianBlur(noisy_image3, 3)
cv2.imshow('Median filter - Impuls noise',blurred3)
cv2.waitKey()
cv2.imwrite("Median filter - Impuls noise.jpg",blurred3)
