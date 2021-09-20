import cv2
import numpy as np

def click(x):
    print(x)

cv2.namedWindow("trackbar")
cv2.createTrackbar("LH", "trackbar", 0, 255, click)
cv2.createTrackbar("UH", "trackbar", 255, 255, click)
cv2.createTrackbar("LS", "trackbar", 0, 255, click)
cv2.createTrackbar("US", "trackbar", 255, 255, click)
cv2.createTrackbar("LV", "trackbar", 0, 255, click)
cv2.createTrackbar("UV", "trackbar", 255, 255, click)


while True:
    #img = np.zeros((250, 250, 3), np.uint8)
    img = cv2.imread("../images/js.JPG")
    resize = cv2.resize(img, (300, 300), cv2.INTER_AREA)
    hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "trackbar")
    uh = cv2.getTrackbarPos("UH", "trackbar")
    ls = cv2.getTrackbarPos("LS", "trackbar")
    us = cv2.getTrackbarPos("US", "trackbar")
    lv = cv2.getTrackbarPos("LV", "trackbar")
    uv = cv2.getTrackbarPos("UV", "trackbar")

    lb = np.array([129, 144, 0])
    ub = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lb, ub)

    res = cv2.bitwise_and(resize, resize, mask=mask)

    cv2.imshow("res", res)

    if cv2.waitKey(20)==ord("q"):
        break

#cap = cv2.VideoCapture("../image/red.mov")
cv2.destroyAllWindows()