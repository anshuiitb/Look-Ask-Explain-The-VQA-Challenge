import cv2 as cv

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)
# can use blur to smooth the image
blur = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Blur', blur)

average = cv.blur(img,(3,3))
cv.imshow('GaussianBlur', blur)

#median blur
median = cv.medianBlur(img,3)
cv.imshow('Median', median)
bilateral = cv.bilateralFilter(img,10,35,35)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)