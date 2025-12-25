# 5 essential functions


# converting to greyscale
import cv2 as cv
img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\park.jpg")

cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cany = cv.Canny(blur, 125, 175) # we use blur to reduce edges basically
cv.imshow('Canny_Edge', cany)

#Dilating the image
dilate = cv.dilate(cany, (3,3), iterations=3)
cv.imshow('Dilate', dilate)

Eroding = cv.erode(dilate, (3,3), iterations=3) # in most cases we get back the dilate to img
cv.imshow('Eroding', Eroding)


#reize and reshape
resize = cv.resize(img,(500,500)) # ignoring the aspect ratio
cv.imshow('Resized', resize)

# cropping
cropped = img[100:500,100:500]
cv.imshow('Cropped', cropped)
cv.waitKey(0)


