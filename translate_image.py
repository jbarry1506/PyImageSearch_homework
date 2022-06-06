import numpy as np
import imutils
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="C:\\Users\\Black Beauty\\Pictures\\LI Motivation\\captain_pirate.jpg", 
    help="path to the picture you want to work with")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("shifted down and right", shifted)

M = np.float32([[1, 0, -10], [0, 1, -20]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("image shifted up and left", shifted)

shifted = imutils.translate(image, -30, -30)
cv2.imshow("shift up left", shifted)
cv2.waitKey(0)
