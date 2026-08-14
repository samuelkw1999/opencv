import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    newframe = cv.Canny(frame, 125, 175)
    cv.imshow('web cam', newframe)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break

video.release()
cv.destroyAllWindows()