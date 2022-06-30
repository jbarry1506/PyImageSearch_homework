"""
Lesson 5
Color Correction
This lesson requires the .cv2contrib virtual environment
- .cv2contrib virtual environment includes:
    - 'opencv-contrib-python' instead of 'opencv-python'
    - 'scikit-image' instead of 'skimage'
"""


import sys
import argparse
import cv2
import imutils
import numpy as np
from imutils.perspective import four_point_transform
from skimage import exposure


def find_color_card(image):
    """
    load the ArUCo dictionary
    grab the ArUCo parameters
    detect the markers in the input image
    """
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image,
        aruco_dict, parameters=aruco_params)

    try:
        ids = ids.flatten()

        i = np.squeeze(np.where(ids == 923))
        topleft = np.squeeze(corners[i])[0]

        i = np.squeeze(np.where(ids == 1001))
        topright = np.squeeze(corners[i])[1]

        i = np.squeeze(np.where(ids == 241))
        bottomright = np.squeeze(corners[i])[2]

        i = np.squeeze(np.where(ids == 1007))
        bottomleft = np.squeeze(corners[i])[3]
    except:
        return None

    card_coords = np.array([
        topleft, topright, bottomright, bottomleft
    ])
    card = four_point_transform(image, card_coords)

    return card


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--reference", required=True,
    help="path to the color reference image")
ap.add_argument("-i", "--input", required=True,
    help="path to the input image to apply the color correction to")
args = vars(ap.parse_args())

ref = cv2.imread(args["reference"])
image = cv2.imread(args["input"])

ref = imutils.resize(ref, width=600)
image = imutils.resize(image, width=600)

cv2.imshow("Reference", ref)
cv2.imshow("Image", image)
# cv2.waitKey(0)

print("[INFO] finding color matching cards...")
refcard = find_color_card(ref)
imagecard = find_color_card(image)

if refcard is None or imagecard is None:
    print("[INFO] could not find color matching card in both images")
    sys.exit(0)

cv2.imshow("Reference Color Card", refcard)
cv2.imshow("Input Color Card", imagecard)

print("[INFO] matching images...")

imagecard = exposure.match_histograms(imagecard, refcard, multichannel=True)

cv2.imshow("Input Color Card After Matching", imagecard)
cv2.waitKey(0)
