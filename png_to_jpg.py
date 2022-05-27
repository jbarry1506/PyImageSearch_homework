from calendar import c
import cv2
import numpy
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="C:\\Users\\Black Beauty\\Documents\\Printing\\halloween_2021.png")
ap.add_argument("-o", "--output", required=False)
args = vars(ap.parse_args())

# print(args["image"])
# print(args["output"])

image_address_split = args["image"].split("\\")
# print(image_address_split[-1])
image_name = image_address_split[-1].split(".")[0]
# print(image_name)

image = cv2.imread(args["image"])
(h, w, c)  = image.shape[:3]

print(f"width: {w} pixels")
print(f"height: {h} pixels")
print(f"channels: {c}")

cv2.imshow(image_name, image)
cv2.waitKey(0)

cv2.imwrite(image_name+".jpg", image)
