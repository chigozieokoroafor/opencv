import cv2
import numpy as np

image = cv2.imread("../images/me (2).JPG")
#image  =  cv2.imread("cd.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# resize all the images to a specific size
scale  = 60
height = int(image.shape[1] * scale/ 100)
width  = int(image.shape[0] * scale/ 100)
resize = cv2.resize(gray, (500, 500), interpolation=cv2.INTER_AREA)
img = resize.copy()
#lap    = cv2.Laplacian(resize, 0)

blur = cv2.blur(resize, (10, 10))
subtracted = cv2.subtract(blur, resize)

kernel = np.ones((1, 1), np.uint8)
dilated = cv2.dilate(resize, kernel)
new = cv2.bitwise_not(subtracted)
newest = cv2.cvtColor(new, cv2.COLOR_GRAY2BGR)
pencil1, pencil2 = cv2.pencilSketch(newest, sigma_s= 2, sigma_r=0.09 , shade_factor=0.09)

#d = cv2.stylization(img, sigma_s=50, sigma_r=0.1)

cv2.imshow("img", img)
cv2.imshow("blur", blur)
cv2.imshow("subtracted", subtracted)
cv2.imshow("new", new)
cv2.imshow("pencil", pencil1)

cv2.waitKey(0)
cv2.destroyAllWindows()