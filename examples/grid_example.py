import numpy as np
import cv2
import np_draw_tools


def main():
    img1 = np.zeros((256, 128, 3), dtype=np.uint8)
    img2 = np.zeros((256, 128, 3), dtype=np.uint8)
    img3 = np.zeros((256, 128, 3), dtype=np.uint8)

    cv2.circle(img1, (64, 40), radius=10, color=(0, 255, 0), thickness=-1)

    img2[:] = 255
    cv2.circle(img2, (5, 60), radius=10, color=(255, 255, 0), thickness=-1)

    img3[:] = 128
    cv2.circle(img3, (128, 69), radius=10, color=(0, 0, 255), thickness=-1)

    grid1 = np_draw_tools.make_grid([img1, img2, img3, img3, img1, img2])
    grid2 = np_draw_tools.make_grid(
        [None, img2, img3, img3, None, img2],
        n_items_in_row=3,
        background_color=(0, 255, 0)
    )

    grid3_images = [
        cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
        for x in [img1, img2, img3, img3, img1, img2]
    ]
    grid3 = np_draw_tools.make_grid(grid3_images, n_items_in_row=2, background_color=15)

    cv2.imshow("grid1", grid1)
    cv2.imshow("grid2", grid2)
    cv2.imshow("grid3", grid3)
    cv2.waitKey()


if __name__ == '__main__':
    main()
