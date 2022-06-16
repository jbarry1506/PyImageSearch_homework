# OpenCV102 - Lesson 3
# Color Spaces

import argparse
from colorsys import hls_to_rgb
import cv2


ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, default="scum-villainy.jpg", help="Look at color spaces for this picture.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("HSV", hsv)
cv2.imshow("L*a*b*", lab)
cv2.imshow("Grayscale", grayscale)

cv2.waitKey(0)
cv2.destroyAllWindows()

hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
cv2.imshow("HLS", hls)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

