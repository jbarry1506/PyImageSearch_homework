"""
Lesson 6B
Detect Low Contrast Video
"""

import argparse
from calendar import c
import imutils
import cv2
import numpy as np
from skimage.exposure import is_low_contrast

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="example_video.mp4", help="path to video file")
ap.add_argument("-t", "--thresh", type=float, default=0.35, help="threshold for low contrast")
args = vars(ap.parse_args())

print("[INFO] accessing video stream...")
vs = cv2.VideoCapture(args["input"] if args["input"] else 0)

while True:
    (grabbed, frame) = vs.read()

    if not grabbed:
        print("[INFO] no frame read from stream - exiting")
        break

    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    text = "Low contrast: No"
    color = (0,255,0)

    if is_low_contrast(gray, fraction_threshold=args["thresh"]):
        text = "Low contrast: Yes"
        color = (0,0,255)
    else:
        cnts = cv2.findContours(frame, [c], -1, (0,255,0), 2)

    cv2.putText(frame, text, (5,25), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    output = np.dstack([edged] * 3)
    output = np.hstack([frame, output])

    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
