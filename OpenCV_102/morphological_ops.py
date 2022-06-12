# Lesson 1-B

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="i_love_paris.png")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

for i in range(0,3):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)
    cv2.imshow(f"Eroded {i+1} times.", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0,3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow(f"Dilated {i+1} times", dilated)

cv2.imshow("Original", image)
cv2.waitKey(0)
