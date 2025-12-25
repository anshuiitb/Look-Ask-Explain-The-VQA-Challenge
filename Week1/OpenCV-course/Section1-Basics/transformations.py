import cv2 as cv
import numpy as np
from sympy.codegen.fnodes import dimension

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\park.jpg")
cv.imshow('park' , img)


#Translation

def translate(img ,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x ---> left, -y---> Up
trans_img = translate(img,-100,-100)
cv.imshow('Translated', trans_img)

#rotation
def rotate(img , angle , rotPoint = None):
    (height , width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rot_img = rotate(img,45)
cv.imshow('Rotated_img', rot_img)
rot = rotate(rot_img,45)
cv.imshow('Rotated', rot)

#Resize
resize = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

#flipping

flip = cv.flip(img,-1)
cv.imshow( 'Flipped', flip)

#cropping
cropped = img[100:300,100:300]
cv.imshow('cropped', cropped)
cv.waitKey(0)
