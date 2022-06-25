"""
Lesson to explain how to use grayscale histograms
"""

# grayscale_histogram
# Usage
# python lesson_1A.py --image beach.png

import argparse
import cv2
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
    default="beach.png", help="image to create histogram from")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Original", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

hist /= hist.sum()

plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
