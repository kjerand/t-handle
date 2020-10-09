import sys

sys.path.append("..")

import numpy as np
from oppgave1.oppgave1_funksjoner import exp
from utils.utils import big, get_h


def euler(X_0, h, n, L, I):

    """
    :param X_0: initialverdi til X.
    :param interval: intervallet til den numeriske løsningen.
    :param n: antall steg.
    :param L: L-vektor (dreiemoment).
    :param I: treghetsmoment
    :return: Liste med punkter som er en tilnærming av den eksakte løsningen
    """
    W = [X_0]

    for i in range(n):
        omega = np.dot(np.linalg.inv(I), np.dot(W[i].T, L))
        Omega = big(omega)
        W.append(np.dot(W[i], exp(h, Omega)))

    return W


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.float)
    h = get_h()
    n = 100
    L = np.array([1, 0, 0], dtype=np.float)
    I = np.identity(3, dtype=np.float)
    W = euler(X_0, h, n, L, I)
    print(W[n]) 
