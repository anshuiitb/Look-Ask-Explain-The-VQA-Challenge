import cv2 as cv

# reading and showing small/normal sized pic
img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cat.jpg")

cv.imshow('cat_pic' , img)
cv.waitKey(0)      # Wait until *any* key is pressed
cv.destroyAllWindows()


#large pic

img2 = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cat_large.jpg")

cv.imshow('cat_large_pic' , img2)
cv.waitKey(0)      # Wait until *any* key is pressed
cv.destroyAllWindows()
# large images often go off-screen

#for video
capture = cv.VideoCapture(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Videos\dog.mp4")
# capture = cv.VideoCapture(0)  used to capture webcam
# for video we have to run a loop frame by frame
# print(type(capture.read())) : is a tuple
while True:
    isTrue , frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()