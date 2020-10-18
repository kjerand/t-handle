import sys

sys.path.append("..")

import numpy as np
from tqdm import tqdm
from oppgave1.oppgave1_funksjoner import exp, energi
from oppgave2.oppgave2 import exactSolution
from utils.utils import big, get_h, max_energy_difference
from tqdm import tqdm


def euler(X_0, interval, n, L, I, initial_energy=0):
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
    energy = [
        initial_energy
        if initial_energy != 0
        else energi(X_0, I, np.dot(np.linalg.inv(np.dot(X_0, I)), L))
    ]

    for i in tqdm(range(n)):
        omega = np.dot(np.linalg.inv(I), np.dot(W[i].T, L))
        Omega = big(omega)
        W.append(np.dot(W[i], exp(h, Omega)))

        new_omega = np.dot(np.linalg.inv(np.dot(W[-1], I)), L)
        new_energy = energi(W[-1], I, new_omega)

        energy.append(new_energy)

        if initial_energy == 0:
            continue

        if np.abs(new_energy - initial_energy) > max_energy_difference:
            print("\n")
            return euler(X_0, interval, n * 2, L, I, initial_energy)

    return W, t, energy, [0]


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.double)
    h = get_h()
    n = 10000
    interval = [0.0, 2.0]
    L = np.array([1, 0, 0], dtype=np.double)
    I = np.identity(3, dtype=np.double)
    W, t, _ = euler(X_0, interval, n, L, I)
    print("Løsning med eulers metode:")
    print(W[n], end="\n\n")

    exact_sol = exactSolution(t)
    print("Eksakt løsning:")
    print(exact_sol[-1])
