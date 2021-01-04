import numpy as np
import matplotlib.pyplot as plt
import cv2

import scipy.ndimage as nd
from scipy import interpolate

def normalize8(img, mode=1):
  img = img.astype(np.float32)
  a, b = img.shape

  max_v_x = img.max()
  min_v_x = img.min()

  if mode == 1:
    normalized_img = np.ceil((( img - min_v_x * np.ones((a, b))) / (max_v_x * np.ones((a, b)) - min_v_x * np.ones((a, b)) ) ) * 255)
  else:
    normalized_img = ( img - min_v_x * np.ones((a, b))) / (max_v_x * np.ones((a, b)) - min_v_x * np.ones((a, b)))
  return normalized_img

def imadjust(x,a,b,c,d,gamma=1):
    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y

def Ihisttruncate(img, lHistCut, uHistCut):
  img = normalize8(img, 0)
  row, column = img.shape
  m = row * column

  sortv_1 = np.sort(img.reshape(-1))
  a = sortv_1[0]
  b = sortv_1[-1]

  sortv_2 = np.concatenate([[a], sortv_1])
  sortv = np.concatenate([sortv_2, [b]])

  x = np.round(100 * (np.arange(0.5, m)) / m, 4)

  x = np.concatenate([[0], x])
  x = np.concatenate([x, [100]])

  gv = np.interp([lHistCut, 100-uHistCut], x.reshape(-1), sortv.reshape(-1))

  new_img = imadjust(img, gv[0], gv[1], 0, 1)
  return new_img