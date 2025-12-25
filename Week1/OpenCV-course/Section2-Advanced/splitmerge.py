import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\park.jpg")

cv.imshow('Park', img)
# cv.imshow('Park', img[:,:,2])

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)
# cv.imshow('Park merged', cv.merge([b,g,r]))


# to view in original color channel
blank = np.zeros(img.shape[:2], np.uint8)
inblue = cv.merge([b, blank, blank])
cv.imshow('InBlue', inblue)
ingreen = cv.merge([blank, g, blank])
cv.imshow('InGreen', ingreen)
inred = cv.merge([blank, blank, r])
cv.imshow('InRed', inred)
cv.waitKey(0)