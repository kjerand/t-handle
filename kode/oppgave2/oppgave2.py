import sys

sys.path.append("..")

import numpy as np


def exactSolution(t):
    return [
        np.array(
            [[1, 0, 0], [0, np.cos(t_i), -np.sin(t_i)], [0, np.sin(t_i), np.cos(t_i)]],
            dtype=np.double,
        )
        for t_i in t
    ]