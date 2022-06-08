# Lesson 9

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="purple-flowers.png", 
    help="Path to the image that you would like to lighten or darken")

args = vars(ap.parse_args())

added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print(f"max of 255: {added}")
print(f"min of 0: {subtracted}")

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 100
lightened = cv2.add(image, M)
cv2.imshow("Lightened", lightened)
cv2.waitKey(0)

M = np.ones(image.shape, dtype="uint8") * 50
darkened = cv2.subtract(image, M)
cv2.imshow("Darkened", darkened)
cv2.waitKey(0)
