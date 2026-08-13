import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3) ,dtype = 'uint8')
blank[:] = 0,0,0
# img = cv.imread('kirby.jpg')
# cv.imshow('img', img)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness = cv.FILLED)
# cv.imshow('green', blank)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness = -1)
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('blue', blank)
cv.waitKey(0)