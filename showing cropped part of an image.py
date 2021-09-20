import cv2
import numpy as np

my_points = []
cropping = True
def onclick1(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), 2, (255, 0, 255), thickness=2)
        my_points.append((x, y))
        if len(my_points)>=2:
            cv2.line(image, my_points[-2], my_points[-1], (255, 255, 255), thickness=1)
        cv2.imshow("image", image)


def onclick2(event, x, y, flags, params):
    global my_points, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x,y), 2, (255, 0, 255), thickness=2)
        my_points.append((x, y))

        if len(my_points)>=2:
            cv2.line(image, my_points[-2], my_points[-1], (255, 255, 255), thickness=1)
            if len(my_points) > 4:
                height, width = 500, 400
                p1 = np.float32([[my_points[0]], [my_points[3]], [my_points[2]], [my_points[1]]])
                p2 = np.float32([[0, 0], [width, 0], [height, width], [0, height]])
                matrix = cv2.getPerspectiveTransform(p1, p2)
                new = cv2.warpPerspective(image, matrix, (width, height))
                cv2.imshow("cut_out", new)
            print(p1)
        cv2.imshow("image", image)


def onclick3(event, x, y, flags, params):
    global cropping, my_points
    if event == cv2.EVENT_LBUTTONDOWN:
        my_points.append((x, y))
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        my_points.append((x, y))
        cropping = False
        cv2.rectangle(image, my_points[0], my_points[1], (255, 0, 0), 3)
        cv2.imshow("image", image)

#image = np.zeros((300, 450), np.uint8)
image = cv2.imread("cd.jpg")
copy = image.copy()


cv2.namedWindow("image")
cv2.setMouseCallback("image", onclick3)



while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1)

    if key == ord("r"):
        image = copy.copy()
    elif key == ord("q"):
        break
    if len(my_points) == 2:
        ROI = copy[my_points[0][1]:my_points[1][1], my_points[0][0]:my_points[1][0]]
        x1 = int(my_points[0][0])
        y1 = int(my_points[0][1])
        x2 = int(my_points[1][0])
        y2 = int(my_points[1][1])
        height, width = 500, 400
        point1 = np.float32([ [x1, y1], [x2, y1], [x2, y2], [x1, y2] ])
        point2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
        matrix = cv2.getPerspectiveTransform(point1, point2)
        warp = cv2.warpPerspective(image, matrix, (width, height))

        cv2.imshow("warp", warp)
        cv2.imshow("roi", ROI)
print(my_points)
cv2.destroyAllWindows()