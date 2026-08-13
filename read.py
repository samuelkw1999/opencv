import cv2 as cv

#rescale image by 75%
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #shape[1] is width of frame, multiply by 0.75 and cast to integer
    height = int(frame.shape[0] * scale) #shape[0] is height of frame, multiply by 0.75 and cast to integer
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#change resolution of live video specifically
def changeRes(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)
    return capture

# img_read = cv.imread('kirby.jpg')
# cv.imshow('kirby', img_read)
# resized_frame = rescaleFrame(img_read)
# cv.imshow('kirby resized', resized_frame)
# cv.waitKey(0)

capture = cv.VideoCapture(0)
reschangedCapture = changeRes(capture,1920,1080)
while (True):
    #isTrue, frame = capture.read()
    isTrue, reschanged_frame = reschangedCapture.read()
    #cv.imshow('video', frame)
    cv.imshow('resolution changed', reschanged_frame)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
reschangedCapture.release()
cv.destroyAllWindows()
