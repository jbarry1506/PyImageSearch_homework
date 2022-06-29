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


# my plots aren't working right
(fig, axs) = plt.subplots(nrows=3, ncols=3, figsize=(8,8))

for (i, image) in enumerate((src, ref, matched)):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

for (j, color) in enumerate(("red", "green", "blue")):
    (hist, bins) = exposure.histogram(image[..., j],
        source_range="dtype")
    axs[j, i].plot(bins, hist / hist.max())

    (cdf, bins) = exposure.cumulative_distribution(image[..., j])
    axs[j, 0].set_ylabel(color)

axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")

plt.tight_layout()
plt.show()
