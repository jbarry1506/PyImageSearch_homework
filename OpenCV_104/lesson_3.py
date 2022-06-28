"""
Lesson 3
Match Histograms
"""

import argparse
import cv2
import matplotlib.pyplot as plt
from skimage import exposure

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,
    help="Source image (The image to transfer the colors to.)")
ap.add_argument("-r", "--reference", required=True,
    help="Path to the input reference image (The image to use as the color reference.")

args = vars(ap.parse_args())

print("[INFO] loading source and reference images . . . ")
src = cv2.imread(args["source"])
ref = cv2.imread(args["reference"])

print("[INFO] performing histogram matching . . .")

multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, multichannel=multi)

cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)
cv2.waitKey(0)
