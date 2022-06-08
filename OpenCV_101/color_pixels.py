# Lesson 2

import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="C:\\Users\\Black Beauty\\Documents\\Printing\\halloween_2020.png", 
    help="<your file path here>")
ap.add_argument("-o", "--output", type=str, default=".")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]

print(f"image[0,0] = blue: {b}, green: {g}, red: {r}")

(b, g, r) = image[250, 250]
print(f"image[250, 250] = blue: {b}, green: {g}, red: {r}")

image[250, 250] = (0, 0, 255)
(b, g, r) = image[250, 250]
print(f"image[250, 250] = blue: {b}, green: {g}, red: {r}")

(cX, cY) = (w//2, h//2)

top_left = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", top_left)

top_right = image[0:cY, cX:w]
cv2.imshow("Top-Right Corner", top_right)

bottom_left = image[cY:h, 0:cX]
cv2.imshow("Bottom-Left Corner", bottom_left)

bottom_right = image[cY:h, cX:w]
cv2.imshow("Bottom-Right Corner", bottom_right)

cv2.imshow("Updated Image", image)
cv2.waitKey(0)
