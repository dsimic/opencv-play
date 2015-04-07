import numpy as np
import cv2

im = cv2.imread('gifts.jpg')
img_gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

img_gray = cv2.GaussianBlur(img_gray, (7, 7), 0)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = np.array([cv2.contourArea(contour) for contour in contours])

min_area = 160.0
max_area = areas.max()

good_contours = [
    contour for idx, contour in enumerate(contours) if areas[idx] > min_area
    and areas[idx] < max_area]


def filter_contour(box):
    return [box]


def min_rect(contour):
    rect = cv2.minAreaRect(contour)
    rect = (
        (rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
    (width, height) = (rect[1][0], rect[1][1])
    print str(width)+" "+str(height)
    box = cv2.cv.BoxPoints(rect)
    box = np.int0(box)
    return box

for contour in good_contours:
    box = contour
    print box
    # box = cv2.approxPolyDP(contour, 10.0, True)
    # box = min_rect(contour)
    perim = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perim, True)
    box = approx
    boxes = filter_contour(box)
    cv2.drawContours(im, boxes, -1, (250, 0, 0), 2)

print "num contours: ", len(good_contours)

cv2.imwrite("outfile.jpg", im)

cv2.imshow('your_image.jpg', im)
cv2.waitKey()
cv2.destroyAllWindows()
