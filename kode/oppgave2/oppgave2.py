import sys

sys.path.append("..")

from oppgave4.RK45 import RK45

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


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.double)
    I = np.identity(3, dtype=np.double)
    omega_0 = np.array([1, 0, 0], dtype=np.double)
    L = np.array([1, 0, 0], dtype=np.double)

    W, t, E = RK45(X_0, [0.0, 20.0], 40000, L, I)

    exact_W = exactSolution(t)

    print(exact_W[-1])
    print(W[-1])