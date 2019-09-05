import numpy as np


def to_int_tuple(point: np.ndarray) -> (int, int):
    assert len(point) == 2
    return int(round(point[0])), int(round(point[1]))
