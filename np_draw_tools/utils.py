import numpy as np


def point_to_int_tuple(point):
    assert len(point) == 2
    return (int(round(point[0])), int(round(point[1])))
