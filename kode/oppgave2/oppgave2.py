import sys

sys.path.append("..")

import numpy as np

"""
1) Vise x_1 = 1, x_2 = x_3 = x_4 = x_7 = 0. Sitter igjen 4 diff likninger.
2) Vise at den roterer om x-aksen pga. vinkelhastighet på x-akse  er 1, og 0 på de andre.
"""


def exactSolution(t):
    return [
        np.array(
            [[1, 0, 0], [0, np.cos(t_i), -np.sin(t_i)], [0, np.sin(t_i), np.cos(t_i)]],
            dtype=np.double,
        )
        for t_i in t
    ]