import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple thresholding
threshold , thresh= cv.threshold(gray, 150 ,255 , cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

threshold , thresh_inv= cv.threshold(gray, 155 ,255 , cv.THRESH_BINARY_INV)
cv.imshow('Threshold_INV', thresh_inv)


#adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV,11,5)
cv.imshow('Adaptive_Thresh', adaptive_thresh)



cv.waitKey(0)