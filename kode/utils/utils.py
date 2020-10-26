import numpy as np
import matplotlib.pyplot as plt


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


max_energy_difference = 2

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

T = 0.000001


def error(W, exact, plot=False):
    errors = np.asarray([errorElem(W[i], exact[i]) for i in range(len(exact))])
    if plot:
        plt.plot([i for i in range(len(W))], errors)
        plt.show()

    return errors


def errorElem(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        return -1

    m1 = matrix1.reshape(-1, 1)
    m2 = matrix2.reshape(-1, 1)
    return sum(np.abs(m1[i] - m2[i]) for i in range(len(m1)))


B = np.array(
    [
        [25 / 216, 0, 1408 / 2565, 2197 / 4104, -1 / 5, 0],
        [16 / 135, 0, 6656 / 12825, 28561 / 56430, -9 / 50, 2 / 55],
    ],
    dtype=np.float,
)

c = np.array([0, 1 / 4, 3 / 8, 12 / 13, 1, 1 / 2], dtype=np.float)
