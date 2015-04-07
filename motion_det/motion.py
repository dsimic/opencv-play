import cv2


def diff_img(t0, t1, t2):
    """
    Computes a differential image.
    """
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


if __name__ == "__main__":

    cam = cv2.VideoCapture(0)

    s, img = cam.read()

    winName = "Movement Indicator"

    cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

    # Read three images first:
    t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    while s:
        cv2.imshow(winName, diff_img(t_minus, t, t_plus))
        # Read next image
        t_minus = t
        t = t_plus
        t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        s, img = cam.read()
        key = cv2.waitKey(10)
        if key == 27:
            cv2.destroyWindow(winName)
            break

    print "Goodbye"
