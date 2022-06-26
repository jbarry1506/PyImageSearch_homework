"""
Lesson 2A
Simple Equalization
"""

import math
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="path to input image")
args = vars(ap.parse_args())

print("[INFO] loading input image . . .")
image = cv2.imread(args["image"])
print(image.shape[0])
print(image.shape[1])
h = math.ceil(image.shape[0] * 0.25)
w =  math.ceil(image.shape[1] * 0.25)
dsize = (w, h)
image = cv2.resize(image, dsize=dsize, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Original Gray", gray)

print("[INFO] performing histogram equalization . . .")
equalized = cv2.equalizeHist(gray)

cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)
