import numpy as np


def get_h():
    return 0.000001


def big(vector):
    return np.array(
        [
            [0, -vector[2], vector[1]],
            [vector[2], 0, -vector[0]],
            [-vector[1], vector[0], 0],
        ],
        dtype=np.float,
    )

max_energy_difference = 0.1

A = np.array(
    [
        [0, 1 / 4, 3 / 32, 1932 / 2197, 439 / 216, -8 / 27],
        [0, 0, 9 / 32, -7200 / 2197, -8, 2],
        [0, 0, 0, 7296 / 2197, 3680 / 513, -3544 / 2565],
        [0, 0, 0, 0, -845 / 4104, 1859 / 4104],
        [0, 0, 0, 0, 0, -11 / 40],
        [0, 0, 0, 0, 0, 0],
    ],
    dtype=np.float,
).T


B = np.array(
    [
        [25 / 216, 0, 1408 / 2565, 2197 / 4104, -1 / 5, 0],
        [16 / 135, 0, 6656 / 12825, 28561 / 56430, -9 / 50, 2 / 55],
    ],
    dtype=np.float,
)

c = np.array([0, 1 / 4, 3 / 8, 12 / 13, 1, 1 / 2], dtype=np.float)