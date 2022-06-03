# lesson 3

import numpy as np
import cv2

cv2canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)

# draw a green diagonal line
cv2.line(cv2canvas, (0, 0), (300, 300), green)

# draw a vertical line
cv2.line(cv2canvas, (150, 0), (150, 300), (200, 100, 100))
cv2.imshow("Drawing Canvas", cv2canvas)


# draw a horizontal line
cv2.line(cv2canvas, (0, 150), (300, 150), (12, 170, 252), 3)
cv2.imshow("Canvas Redrawn", cv2canvas)


# draw a circle
cv2.circle(cv2canvas, (150, 150), 75, (27, 119, 228), 7)
cv2.imshow("Canvas Circle", cv2canvas)
cv2.waitKey()


# draw a rectangle
cv2.rectangle(cv2canvas, (125, 125), (225, 225), (190, 52, 207), -1)
cv2.imshow("filled square", cv2canvas)
cv2.waitKey()
