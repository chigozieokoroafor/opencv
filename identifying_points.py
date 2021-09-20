import cv2
import numpy as np

def onclick(event, x, y, flag, param):

    if event==cv2.EVENT_LBUTTONDOWN:
        text = str(x) +","+str(y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, (x, y), font, 0.5, (255, 255, 255), thickness=1)
        cv2.imshow("image", image)
    if event == cv2.EVENT_RBUTTONDOWN:
        # joining points

        cv2.circle(image, (x, y), 2, (255, 255, 255), -1)
        point.append((x, y))
        if len(point)>=2:
            cv2.line(image, point[-2], point[-1], (255, 0, 0), thickness=3)
        cv2.imshow('image', image)
#image = cv2.imread("")
image = np.zeros((500, 500), np.uint8)
point = []
cv2.imshow("image", image)
cv2.setMouseCallback("image", onclick)

cv2.waitKey(0)
cv2.destroyAllWindows()
