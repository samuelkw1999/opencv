import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('kirby.jpg')
img = cv.resize(img, (500,500))

# plt.imshow(img)
# plt.show()

#BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#BGR TO HSV (hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

#BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) 

#CANNOT CONVERT GRAYSCALE TO HSV, MUST CONVERT TO BGR FIRST, THEN TO HSV
#i assume its the same for all other color spaces, bgr is the default

# cv.imshow('gray', gray)
cv.imshow('RGB', rgb)
cv.imshow('LAB', lab)
cv.imshow('hsv', hsv)
plt.imshow(rgb)
plt.show()
cv.waitKey(0)