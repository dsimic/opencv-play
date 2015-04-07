import cv2
import numpy as np


frame = cv2.imread('gifts.jpg')

img_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# lower = np.array([0, 0, 0], np.uint8)
# upper = np.array([10, 10, 10], np.uint8)

# separated = cv2.inRange(img, lower, upper)

ret, separated = cv2.threshold(img_grey, 127, 255, 0)

# this bit draws a red rectangle around the detected region

contours, hierarchy = cv2.findContours(
    separated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0

largest_contour = None

for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        largest_contour = contour
        if largest_contour is not None:
            moment = cv2.moments(largest_contour)
            print contour
            if moment["m00"] > 100:
                rect = cv2.minAreaRect(largest_contour)
                rect = (
                    (rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
                (width, height) = (rect[1][0], rect[1][1])
                print str(width) + " " + str(height)
                box = cv2.cv.BoxPoints(rect)
                box = np.int0(box)
                if height > 0.9 * width and height < 1.1 * width:
                    cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
                else:
                    cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

cv2.imshow('dst', frame)

if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
