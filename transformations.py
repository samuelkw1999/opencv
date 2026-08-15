import cv2 as cv
import numpy as np


img = cv.imread('kirby.jpg')

def translate(img, x , y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)

#rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] #grabbing height and width and putting them in the tuple

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

#resize image again?
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)
cv.imshow('resize', resized)

#flip image
flip = cv.flip(img, -1)
cv.imshow('flip', flip)

#crop image
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)

rotated = rotate(img, 45)
cv.imshow('rotated kirby', rotated)

cv.imshow('kirby', translated)
cv.waitKey(0)

