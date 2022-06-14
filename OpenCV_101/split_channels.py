# Lesson 12

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv.png",
    help="Image to split colors.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(B,G,R) = cv2.split(image)

cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)
cv2.waitKey(0)
cv2.destroyAllWindows()

