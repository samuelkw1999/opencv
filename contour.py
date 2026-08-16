import cv2 as cv
import numpy as np

img = cv.imread('kirby.jpg')
img = cv.resize(img, (500,500))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

#threshold method
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #tries turning image into binary, black and white image

#find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 
#RETR_EXTERNAL will return only external contours, retr tree will return all of them
#chain approx none will not compress coordinates, approx simple will compress coordinates to endpoints of a line
print(f'{len(contours)} contours found')

#draw the contours that open cv found
blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours drawn onto blank image', blank)

cv.imshow('cannyedges', canny)
cv.imshow('thresh', thresh)
cv.imshow('graykirby', gray)
cv.imshow('kirby',img)
cv.waitKey(0)