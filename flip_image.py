# lesson 6

import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, default="tree_cliff.png", help="Path to image to flip.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

flipped_horizontal = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped_horizontal)
cv2.waitKey(0)

flipped_vertical = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped_vertical)
cv2.waitKey(0)

flipped_both = cv2.flip(image, -1)
cv2.imshow("Flipped Both Ways", flipped_both)
cv2.waitKey(0)
