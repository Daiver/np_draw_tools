import numpy as np
import cv2
import np_draw_tools


def main():
    # point to int tuple
    pt = [0.34, 0.6]
    print(np_draw_tools.point_to_int_tuple(pt))
    pt = np.array([0.34, 0.6])
    print(np_draw_tools.point_to_int_tuple(pt))


if __name__ == '__main__':
    main()
