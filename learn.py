import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale) #shape[1] is width of frame, multiply by 0.75 and cast to integer
    height = int(frame.shape[0] * scale) #shape[0] is height of frame, multiply by 0.75 and cast to integer
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread('kirby.jpg')
img = rescaleFrame(img) #rescale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)#turn to grayscale

#blur
blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('CANNY EDGES', canny)

#dilate image
dilated = cv.dilate(canny, (3,3), iterations = 3)
# cv.imshow('dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations = 3)
# cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500))
cv.imshow('resized', resized)

#crop the array
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

# cv.imshow('grayscale', gray)
# cv.imshow('blur', blur)
cv.imshow('original', img)
cv.waitKey(0)