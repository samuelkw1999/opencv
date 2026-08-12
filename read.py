import cv2 as cv

""" img_read = cv.imread('images/kirby.jpg')

cv.imshow('kirby', img_read) """

video = cv.VideoCapture(0)

while (True):
    isTrue, frame = video.read()
    cv.imshow('video', frame)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break

video.release()
cv.destroyAllWindows()

#cv.waitKey(0)