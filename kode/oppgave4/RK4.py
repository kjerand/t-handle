import sys

sys.path.append("..")

import numpy as np
from tqdm import tqdm
from oppgave1.oppgave1_funksjoner import exp, energi
from utils.utils import get_h, big, max_energy_difference


def RK4(X_0, interval, n, L, I, initial_energy=0):
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
    energy = [
        initial_energy
        if initial_energy != 0
        else energi(X_0, I, np.dot(np.linalg.inv(np.dot(X_0, I)), L))
    ]

    for i in tqdm(range(n)):
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

        new_omega = np.dot(np.linalg.inv(np.dot(W[-1], I)), L)
        new_energy = energi(W[-1], I, new_omega)
        energy.append(new_energy)

        if initial_energy == 0:
            continue

        if np.abs(new_energy - initial_energy) > max_energy_difference:
            return RK4(X_0, interval, n * 2, L, I, initial_energy)

    return W, t, energy, [0]


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