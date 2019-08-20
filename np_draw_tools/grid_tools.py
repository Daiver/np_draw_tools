import numpy as np


def make_grid(images, n_items_in_row=None):
    n_images = len(images)
    assert n_images > 0
    if n_items_in_row is None:
        n_items_in_row = n_images

    n_rows = np.ceil(n_images / n_items_in_row)
    image_shape = images[0].shape
    assert len(image_shape) in [2, 3]
    if len(image_shape) == 3:
        res_shape = (int(image_shape[0] * n_rows), int(image_shape[1] * n_items_in_row), image_shape[2])
    else:
        res_shape = (int(image_shape[0] * n_rows), int(image_shape[1] * n_items_in_row))
    res = np.zeros(res_shape, dtype=images[0].dtype)

    for ind, image in enumerate(images):
        row = ind // n_items_in_row
        col = ind % n_items_in_row
        res[
            row * image_shape[0]: (row + 1) * image_shape[0],
            col * image_shape[1]: (col + 1) * image_shape[1]
        ] = image

    return res
