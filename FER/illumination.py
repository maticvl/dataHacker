from functions import normalize8, Ihisttruncate
import cv2
import numpy as np

def gamma_correction(img, gamma):
  gamma_img = np.power(img.astype(np.float32) / 255.0, gamma)
  return gamma_img

def DoG(img, sigma_zero=1, sigma_one=2, normalization=1):
  img = normalize8(img)
  
  blurred_img0 = cv2.GaussianBlur(img, (int(2*np.ceil(3*sigma_zero)+1), int(2*np.ceil(3*sigma_zero)+1)), sigma_zero)
  blurred_img1 = cv2.GaussianBlur(img, (int(2*np.ceil(3*sigma_one)+1), int(2*np.ceil(3*sigma_one)+1)), sigma_one)
  
  img = blurred_img0 - blurred_img1  

  if normalization != 0:
    img = Ihisttruncate(img, 0.2, 0.2)
    img_clipped = np.clip(img, 0, 1)
    img = normalize8(img_clipped)
  return img

def robust_postprocessor(img, gamma=0.2, sigma_one=1, sigma_two=2, alfa=0.1, tau=10):
  gamma_img = gamma_correction(img, gamma)
  img_dog = DoG(gamma_img, sigma_one, sigma_two)
  a, b = img_dog.shape
  img = img_dog / (np.mean((np.abs(img_dog)) ** alfa) ** (1 / alfa))
  img = img / (np.mean(np.minimum(tau * np.ones((1, a * b)), np.abs(img.reshape(-1))) ** alfa) ** (1 / alfa))

  new_img = tau * np.tanh(img / tau)
  new_img = (normalize8(new_img)).astype(np.uint8)

  return new_img