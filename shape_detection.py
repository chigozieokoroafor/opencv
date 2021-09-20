import cv2
import numpy as np

image = cv2.imread("../images/IMG_0007.JPG")
canvas = np.ones((500, 500), np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resize = cv2.resize(gray, (500, 400), interpolation=cv2.INTER_AREA)
res = cv2.resize(image, (500, 400))
_, th = cv2.threshold(resize, 125, 255, 0)
contours, heirarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for contour in contours:

    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(canvas, [approx], -1, (255, 45, 0), thickness=1)
    x, y, w, h = cv2.boundingRect(approx)
    #if len(approx) == 3:
    #    cv2.putText(canvas, "triangle", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (234))
    if len(approx) == 4:
        aspect_ratio = float(w)/h
        if aspect_ratio>=0.95 and aspect_ratio<=1.05:
           cv2.putText(canvas, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200))
        else:
            cv2.putText(canvas, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200))
    if len(approx) > 4:
        cv2.putText(canvas, "circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200))
cv2.imshow("image", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()