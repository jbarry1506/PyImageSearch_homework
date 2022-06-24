# OpenCV102 7B
# opencv_sobel_scharr.py

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="coins02.png", help="path to input image")
ap.add_argument("-s", "--scharr", type=int, default=0, help="path to input image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

ksize = -1 if args["scharr"] > 0 else 3
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr Combined", combined)
cv2.waitKey(0)
