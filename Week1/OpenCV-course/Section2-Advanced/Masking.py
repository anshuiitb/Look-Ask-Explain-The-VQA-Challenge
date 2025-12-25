import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow('blank', blank)

mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2+200, img.shape[0]//2+200), color=(255,255,255), thickness=-1)
cv.imshow('Circle', mask)


masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked_img', masked_img)
cv.waitKey(0)