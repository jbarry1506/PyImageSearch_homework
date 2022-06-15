# OpenCV 102: Lesson 2-B
# Bilateral Smoothing and Blurring

import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, default="scum-villainy.jpg")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# (diameter, sigma_color, sigma_space)
params = [(11,21,7), (11,41,21), (11,61,39)]

for (diameter, sigma_color, sigma_space) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor=sigma_color, sigmaSpace=sigma_space)
    title = f"Blurred {diameter},{sigma_color},{sigma_space}"
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
