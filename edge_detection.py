import cv2
import numpy as np

image = cv2.imread("cd.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (2, 2))

canny = cv2.Canny(blur, 10, 255)

other = cv2.bitwise_and(blur, canny)
new = cv2.bitwise_not(other)
cv2.imshow("image", new)

cv2.waitKey(0)
cv2.destroyAllWindows()