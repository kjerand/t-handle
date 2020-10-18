import sys

sys.path.append("..")

import numpy as np
from tqdm import tqdm
from oppgave1.oppgave1_funksjoner import exp
from utils.utils import big, get_h
from tqdm import tqdm


def euler(X_0, interval, n, L, I):
    """
    :param X_0: initialverdi til X.
    :param interval: intervallet til den numeriske løsningen.
    :param n: antall steg.
    :param L: L-vektor (dreiemoment).
    :param I: treghetsmoment
    :return: Liste med punkter som er en tilnærming av den eksakte løsningen
    """

    h = float((interval[1] - interval[0]) / n)
    t = [i * h for i in range(n + 1)]
    W = [X_0]

    for i in tqdm(range(n)):
        omega = np.dot(np.linalg.inv(I), np.dot(W[i].T, L))
        Omega = big(omega)
        W.append(np.dot(W[i], exp(h, Omega)))

    return W, t, [0]


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.double)
    h = get_h()
    n = 10000
    interval = [0.0, 2.0]
    L = np.array([1, 0, 0], dtype=np.double)
    I = np.identity(3, dtype=np.double)
    W, t, _ = euler(X_0, interval, n, L, I)
    print(W[n])
