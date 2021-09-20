import cv2
import numpy as np
#image = cv2.imread("../images/chi3_face.jpg")
image = cv2.imread("cd.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resize = cv2.resize(gray, (400, 400), interpolation=cv2.INTER_AREA)
blur_image = cv2.blur(resize, (5, 5))
#edge = cv2.Canny(blur_image, 1, 255)
sobel_x = cv2.Sobel(blur_image, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(blur_image, cv2.CV_64F, 0, 1)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

edge = cv2.bitwise_or(sobel_x, sobel_y)
final =  cv2.bitwise_and(edge, resize)
kernel = np.ones((1, 1), np.uint8)
#dilated = cv2.dilate(final, kernel)
eroded = cv2.erode(final, kernel)

#no = cv2.bitwise_not(eroded)
no = cv2.cvtColor(eroded, cv2.COLOR_GRAY2BGR)
pencil, _ = cv2.pencilSketch(no, sigma_s= 2, sigma_r=0.09 , shade_factor=0.09)
cv2.imshow("image", _)
cv2.waitKey(0)
cv2.destroyAllWindows()
