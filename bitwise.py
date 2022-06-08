# Lesson 10

import numpy as np
import cv2

rect = np.zeros((300,300), dtype="uint8")
cv2.rectangle(rect, (25,25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rect)

circ = np.zeros((300, 300), dtype="uint8")
cv2.circle(circ, (150,150), 150, 255, -1)
cv2.imshow("Circle", circ)

bitwiseAnd = cv2.bitwise_and(rect, circ)
cv2.imshow("Bitwise And", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rect, circ)
cv2.imshow("Bitwise Or", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rect, circ)
cv2.imshow("Bitwise Xor", bitwiseXor)

bitwiseNot = cv2.bitwise_not(circ, rect)
cv2.imshow("Bitwise Not", bitwiseNot)
cv2.waitKey(0)
