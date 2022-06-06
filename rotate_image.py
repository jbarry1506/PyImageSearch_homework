from inspect import Arguments
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, default=".\\tree_cliff.png", 
    help="Choose an image to rotate.", required=False)

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w//2, h//2)
print(f"h={h}, w={w}, cX={cX}, cY={cY}")

M = cv2.getRotationMatrix2D((cX, cY), 45, .33)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated", rotated)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
clockwise90 = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Clockwise 90 degrees", clockwise90)

M = cv2.getRotationMatrix2D((-100, -100), 20, .5)
outside_rotation = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Outside Rotation", outside_rotation)

inverted = imutils.rotate(image, 180)
cv2.imshow("Inverted Image", inverted)

bound_rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated without cropping", bound_rotated)
cv2.waitKey(0)
