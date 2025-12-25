import cv2 as cv

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cat.jpg")
cv.imshow('cat_pic' , img)
cv.waitKey(0)      # Wait until *any* key is pressed
cv.destroyAllWindows()


#rescaling : suggested to downscale
def rescaleFrame(frame, scale=0.25):
    #works for LIVE , VIDEO , IMAGE
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions,interpolation=cv.INTER_AREA)


img2 = cv.imread('/Week1/OpenCV-course/Resources/Photos/cat_large.jpg')

cv.imshow('cat_pic_large' , img2)
cv.waitKey(0)
cv.destroyAllWindows()

re = rescaleFrame(img2)
cv.imshow('cat_rescaled' , re)
cv.waitKey(0)
cv.destroyAllWindows()


#for video

capture = cv.VideoCapture(r"/Week1/OpenCV-course\Resources\Videos\dog.mp4")

while True:
    isTrue , frame = capture.read()
    res=rescaleFrame(frame,scale=0.2)
    cv.imshow('video', frame)
    cv.imshow('rescaled_video',res)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


#another method to rescale , for live videos i.e. capture.set method

def changeRes(width,height):
    #  works for LIVE VIDEO only 
    capture.set(3,width)
    capture.set(4,height)
