# lesson 7

import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="zombies.png", help="path to the image to crop")
ap.add_argument("-o", "--output", type=str, default=".", help="path to the save location", required=False)

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original Sprite Sheet", image)
cv2.waitKey(0)

jim_zombie = image[148:287, 82:151]
cv2.imshow("jim zombie", jim_zombie)
cv2.waitKey(0)
lauren_zombie = image[302:428, 527:604]
cv2.imshow("lauren_zombie", lauren_zombie)
cv2.waitKey(0)

jz_flipped = cv2.flip(jim_zombie, 1)
cv2.imshow("", jz_flipped)
cv2.imshow("", lauren_zombie)
cv2.waitKey(0)

jz_flipped_resized = imutils.resize(jz_flipped, 450)
cv2.imshow("jim zombie loves . . . ", jz_flipped_resized)
cv2.waitKey(0)

lz_resized = imutils.resize(lauren_zombie, 450)
cv2.imshow("lauren zombie . . . 4 EVER!!!", lz_resized)
cv2.waitKey(0)
