import cv2 as cv
import numpy as np

# img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\lady.jpg")
# cv.imshow('Original', img)
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# haar_cascade = cv.CascadeClassifier('haar_face.xml')
#
# faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.1, minNeighbors = 3)
# print(f"{len(faces_rect)} , faces_rect ={faces_rect}")
#
#
#
# for (x, y, w, h) in faces_rect:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv.imshow('faces_rect', img)
#
#
#
# cv.waitKey(0)


img2 = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\group 1.jpg")
cv.imshow('Original', img2)


gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray2)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray2 , scaleFactor=1.1, minNeighbors=1)

print(f"Number of faces detected: {len(face_rect)}")

for (x,y,w,h) in face_rect:
    cv.rectangle(img2, (x,y), (x+w,y+h), (255,0,0), 2)

cv.imshow("rect", img2)
cv.waitKey(0)