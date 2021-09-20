import time
import cv2
import numpy as np

cap = cv2.VideoCapture("../images/red_1.MOV")

count = 0
background = 0

#capturing the image in the range of 60
for i in range(1):
    ret , background = cap.read()
    #background = np.flip(background, axis=1)

while cap.isOpened():
    ret, image = cap.read()
    print(ret)
    if not ret:
        break
    count += 1
    #image = np.flip(image, axis=1)
    #convert to HSV color_space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # generate mask
    lower_red = np.array([0, 125, 50])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)


    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2



    #open and dilate the masked image
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    mask_inv = cv2.bitwise_not(mask)


    # segmenting the redcolour part out of the frame
    res1 = cv2.bitwise_and(image, image, mask= mask_inv)

    res2 = cv2.bitwise_and(background, background, mask= mask)

    cv2.imshow("res1", res1)
    cv2.imshow("res2", res2)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()