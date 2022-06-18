# OpenCV102 - Lesson 4-A

import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="coins01.png", 
    help="Create thresholds of this picture.")

args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imshow("Grayed and Blurred", blurred)

(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

(T, threshBin) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", threshBin)

masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)
