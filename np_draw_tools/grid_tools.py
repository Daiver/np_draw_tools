from typing import Union, List, Tuple
import numpy as np


def make_grid(
        images: List[np.ndarray],
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

    n_rows = np.ceil(n_images / n_items_in_row)
    first_not_none_image = next(image for image in images if image is not None)
    image_shape = first_not_none_image.shape
    assert len(image_shape) in [2, 3]
    if len(image_shape) == 3:
        res_shape = (int(image_shape[0] * n_rows), int(image_shape[1] * n_items_in_row), image_shape[2])
    else:
        res_shape = (int(image_shape[0] * n_rows), int(image_shape[1] * n_items_in_row))
    res = np.zeros(res_shape, dtype=first_not_none_image.dtype)
    res[:, :] = background_color

    for ind, image in enumerate(images):
        if image is None:
            continue
        row = ind // n_items_in_row
        col = ind % n_items_in_row
        res[
            row * image_shape[0]: (row + 1) * image_shape[0],
            col * image_shape[1]: (col + 1) * image_shape[1]
        ] = image

    return res
