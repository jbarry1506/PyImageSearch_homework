"""
Lesson 6
Low Contrast Photo Detection
"""

import argparse
from calendar import c
import imutils
import cv2
from imutils.paths import list_images
from skimage.exposure import is_low_contrast

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=True,
    help="path to input directory of images")
ap.add_argument("-t", "--thresh", type=float, default=0.35,
    help="threshold for low contrast")
args = vars(ap.parse_args())

image_paths = sorted(list(list_images(args["directory"])))

for (i, image_path) in enumerate(image_paths):
    print(f"[INFO] processing image {i+1}/{len(image_paths)}")
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=450)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    text = "Low contrast: No"
    color = (0, 255, 0)

    if is_low_contrast(gray, fraction_threshold=args["thresh"]):
        text = "Low contrast: Yes"
        color = (0, 0, 255)
    else:
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)

        cv2.drawContours(image, [c], -1, (0,255,0), 2)

    cv2.putText(image, text, (5,25), cv2.FONT_HERSHEY_SIMPLEX, color, 2)

    cv2.imshow("Image", image)
    cv2.imshow("Edge", image)
    cv2.waitKey(0)
