# Lesson 5

import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=".\\tree_cliff.png", 
    help="The path to the image you want to resize.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

(h, w) = image.shape[:2]

r = 150.0 / w
dim = (150, int(h * r))
resized_by_width = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized by width", resized_by_width)
cv2.waitKey(0)

r = 600.0 / h
dim = (int(w * r), 600)
resized_by_height = cv2.resize(image, dim, interpolation=cv2.INTER_BITS)
cv2.imshow("resized by height", resized_by_height)
cv2.waitKey(0)


r = 600.0 / h
dim = (int(w * r), 600)
resized_by_height2 = cv2.resize(image, dim, interpolation=cv2.INTER_BITS2)
cv2.imshow("resized by height2", resized_by_height2)
cv2.waitKey(0)

# complete list of interpolation methods for resizing images
# https://iq.opengenus.org/different-interpolation-methods-in-opencv/
methods_list = [
    ("INTER_NEAREST", cv2.INTER_NEAREST) ,
    ("INTER_LINEAR", cv2.INTER_LINEAR) ,
    ("INTER_LINEAR_EXACT", cv2.INTER_LINEAR_EXACT) ,
    ("INTER_AREA", cv2.INTER_AREA) ,
    ("INTER_CUBIC", cv2.INTER_CUBIC) ,
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4) ,
    ("INTER_MAX", cv2.INTER_MAX)
    # ("WARP_FILL_OUTLIERS", cv2.WARP_FILL_OUTLIERS) ,
    # ("WARP_INVERSE_MAP", cv2.WARP_INVERSE_MAP)
]

for (name, method) in methods_list:
    print(f"[INFO]:  {name}")
    resized = imutils.resize(image, width=(w * 2), inter=method)
    cv2.imshow(f"Image Resized With {method}", resized)
    cv2.waitKey(0)
