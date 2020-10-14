import sys

sys.path.append("..")

import numpy as np
from oppgave1.oppgave1_funksjoner import exp
from oppgave3.euler import euler
from utils.utils import get_h, big


def RK4(X_0, interval, n, L, I):
    """
    :param X_0: initialverdi til X.
    :param h: stegstørrelse.
    :param n: antall steg.
    :param L: L-vektor (dreiemoment).
    :param I: treghetsmoment
    :return: Liste med punkter som er en tilnærming av den eksakte løsningen
    """

    h = float((interval[1] - interval[0]) / n)
    t = [i * h for i in range(n + 1)]
    W = [X_0]
    for i in range(n):
        sigma_1 = np.dot(np.linalg.inv(I), np.dot(W[i].T, L))
        sigma_2 = sigma_i(big(sigma_1), h, I, W[i], L)
        sigma_3 = sigma_i(big(sigma_2), h, I, W[i], L)
        sigma_4 = sigma_i(big(sigma_3), 2 * h, I, W[i], L)
        W.append(
            np.dot(
                W[i],
                exp(
                    (h / 6),
                    big(sigma_1) + 2 * big(sigma_2) + 2 * big(sigma_3) + big(sigma_4),
                ),
            )
        )
    return W, t, [0]


def sigma_i(Sigma, h, I, W, L):
    return np.dot(np.dot(np.linalg.inv(I), exp(-(h / 2), Sigma)), np.dot(W.T, L))


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.float)
    h = get_h()
    n = 1000
    L = np.array([1, 0, 0], dtype=np.float)
    I = np.identity(3, dtype=np.float)
    interval = [0.0, 10.0]
    W_r = RK4(X_0, interval, n, L, I)
    W_e = euler(X_0, h, n, L, I)
    print(abs(W_r[n] - W_e[n]))