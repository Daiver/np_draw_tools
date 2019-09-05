import cv2


def wait_esc():
    key = cv2.waitKey()
    while key % 255 != 27:
        key = cv2.waitKey()
