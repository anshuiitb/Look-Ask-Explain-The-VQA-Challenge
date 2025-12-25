import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



blank = np.zeros(img.shape[:2], np.uint8)

circle = cv.circle (blank,(blank.shape[1]//2,blank.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow('Mask', mask)
# gray scale histogram

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


#color histogram
colors = ('b','g','r')

plt.figure()
plt.title('color Histogram')

for i,color in enumerate(colors):
    print(f"Histogram for color {color} and i is {i}")
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)