"""
Lesson 2B
Adaptive Equalization
"""

import math
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="path to input image")
ap.add_argument("-c", "--clip", type=float, default=2.0, help="threshold for contrast limiting")
ap.add_argument("-t", "--tile", type=int, default=8, help="tile grid size -- divides image into tile x tile cells")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
if image.shape[0] > 720 or image.shape[1] > 1080:
    image = cv2.resize(image, dsize=(720, 1080), interpolation=cv2.INTER_AREA)
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("[INFO] applying CLAHE . . . ")
clahe = cv2.createCLAHE(clipLimit=args["clip"],
    tileGridSize=(args["tile"], args["tile"]))

# color adjustment not working?  Does Clahe only work on gray?
# equalized = clahe.apply(image)
# cv2.imshow("Equalized Color", equalized)
equalized_gray = clahe.apply(gray)
cv2.imshow("Equalized Gray", equalized_gray)

cv2.waitKey(0)

