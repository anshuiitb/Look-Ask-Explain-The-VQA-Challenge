import cv2 as cv
import numpy as np

blanks = np.zeros((500,500,3),dtype='uint8') # to make blank page
cv.imshow('Blank_img', blanks)

#paint a image certain color
blanks[200:300 , 300:400]=0,255,0 # make it green (drawing it green)

# cv.imshow('Green_img', blanks)
# cv.waitKey(0)
# cv.destroyAllWindows()

#we can use the image of cat also in the same manner
# cv.rectangle(blanks, (0,0), (250,500), color=(0,255,0), thickness=-1)
cv.rectangle(blanks, (0,0), (blanks.shape[1]//2 , blanks.shape[0]//2), color=(0,255,0), thickness=-1)
cv.imshow('Rectangle_img', blanks)

# 3 circle
cv.circle(blanks, (blanks.shape[1]//2 , blanks.shape[0]//2) , 40 , color=(0,0,255), thickness=-1)
cv.imshow('Circle', blanks)

#line
cv.line(blanks , (0,0) , (blanks.shape[1]//2 , blanks.shape[0]//2), color =(255,255,255), thickness=2)
cv.imshow('Line', blanks)
#text
cv.putText(blanks , 'Hello' , (120,225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255,0), thickness=2)
cv.imshow('Text', blanks)
cv.waitKey(0)