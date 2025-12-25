import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)

# plt.imshow(img)
# plt.show()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
#BGR to RGB
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR and then BGR to lab, we can't directly convert lab to hsv or hsv to lab

# cv.waitKey(0)
plt.imshow(rgb)
plt.show()