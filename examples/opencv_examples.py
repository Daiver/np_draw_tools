import numpy as np
import cv2

import np_draw_tools


def main():
    canvas = np.zeros((256, 256, 3), dtype=np.uint8)
    cv2.circle(canvas, (128, 129), 10, (0, 255, 0), 5)
    cv2.imshow("", canvas)
    np_draw_tools.wait_esc()


if __name__ == '__main__':
    main()
