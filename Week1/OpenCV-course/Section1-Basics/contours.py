import cv2 as cv
import numpy as np
from torch.utils.model_dump import hierarchical_pickle

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)
blank = np.zeros(img.shape, np.uint8)
# cv.imshow('Blank', blank)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
#
# canny = cv.Canny(blur ,100,200)
# cv.imshow('Canny', canny)
ret , thresh = cv.threshold(gray,125 , 255,cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
contours , hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
