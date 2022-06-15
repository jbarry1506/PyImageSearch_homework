# OpenCV 102 Lesson 2-A
# Blurring

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="scum-villainy.jpg")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernel_sizes = [(3,3), (9,9), (15,15)]

for (kX, kY) in kernel_sizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow(f"Gaussian ({kX}, {kY})", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for k in (3,9,15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median {k}", blurred)
    cv2.waitKey(0)