from typing import Union, List, Tuple
import numpy as np


def make_grid(
        images: Union[List[np.ndarray], np.ndarray],
        n_items_in_row: int = None,
        background_color: Union[int, float, Tuple[int, int, int]] = None,
        margin: int = 0
):
    n_images = len(images)
    assert n_images > 0
    if n_items_in_row is None:
        n_items_in_row = n_images
    if background_color is None:
        background_color = 0

    n_rows = int(np.ceil(n_images / n_items_in_row))
    first_not_none_image = next(image for image in images if image is not None)
    image_shape = first_not_none_image.shape
    assert len(image_shape) in [2, 3]

    res_width = image_shape[1] * n_items_in_row + (n_items_in_row - 1) * margin
    res_height = image_shape[0] * n_rows + (n_rows - 1) * margin
    res_shape = (res_height, res_width)
    if len(image_shape) == 3:
        res_shape = (res_height, res_width, image_shape[2])

    res = np.zeros(res_shape, dtype=first_not_none_image.dtype)
    res[:, :] = background_color

    for ind, image in enumerate(images):
        if image is None:
            continue
        row = ind // n_items_in_row
        col = ind % n_items_in_row

        row_offset = 0 if row == 0 else margin * row
        col_offset = 0 if col == 0 else margin * col

        res[
            row * image_shape[0] + row_offset: (row + 1) * image_shape[0] + row_offset,
            col * image_shape[1] + col_offset: (col + 1) * image_shape[1] + col_offset
        ] = image

    return res
