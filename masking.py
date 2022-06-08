# Lesson 11

import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="zombies.png", help="Path to the image that you want to mask.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (5,150), (300,300), 255, -1)
cv2.imshow("Rectangular Mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (260,178), 25, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Circle Mask", mask)
cv2.imshow("Circle Mask Applied", masked)
cv2.waitKey(0)
