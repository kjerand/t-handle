import sys

sys.path.append("..")

import numpy as np
from tqdm import tqdm
from oppgave1.oppgave1_funksjoner import exp, energi
from oppgave2.oppgave2 import exactSolution
from oppgave3.euler import euler
from oppgave4.RK4 import RK4
from utils.utils import get_h, big, A, B, c, max_energy_difference
from tqdm import tqdm


def RK45(X_0, interval, n, L, I, initial_energy=0):
    """
    :param X_0: initialverdi til X.
    :param interval: start og sluttidspunkt for beregningen
    :param n: antall steg.
    :param L: L-vektor (dreiemoment).
    :param I: treghetsmoment
    :return: Liste med punkter som er en tilnærming av den eksakte løsningen
             Liste med tidspunkter som samsvarer med punktene
             Liste med energien i systemet ved de ulike tidspunktene
             Liste med feilestimatet E som vist i kapittel 4.5 i oppgaven
    """
    h = float((interval[1] - interval[0]) / n)
    t = [i * h for i in range(n + 1)]
    W = [X_0]
    Z = [X_0]
    E = [0]
    energy = [
        initial_energy
        if initial_energy == 0
        else energi(X_0, I, np.dot(np.linalg.inv(np.dot(X_0, I)), L))
    ]

    for i in tqdm(range(0, n)):  # O(n)
        sigmas = [np.dot(np.linalg.inv(I), np.dot(W[i].T, L))]
        for j in range(5):
            nextSigma = 0
            for k in range(j + 1):
                nextSigma += A[j + 1, k] * big(sigmas[k])
            sigmas.append(sigma(I, W[i], L, h, nextSigma))

        W.append(
            np.dot(
                W[i],
                exp(h, sum(B[0, i] * big(sigmas[i]) for i in range(6))),
            ),
        )
        Z.append(
            np.dot(
                W[i],
                exp(h, sum(B[1, i] * big(sigmas[i]) for i in range(6))),
            ),
        )

        deltaW = W[-1] - Z[-1]
        E.append(np.sqrt(np.trace(np.dot(deltaW.T, deltaW))))

        new_omega = np.dot(np.linalg.inv(np.dot(W[-1], I)), L)
        new_energy = energi(W[-1], I, new_omega)
        energy.append(new_energy)

        if initial_energy == 0:
            continue

        if np.abs(new_energy - initial_energy) > max_energy_difference:
            return RK45(X_0, interval, n * 2, L, I, initial_energy)
    return W, t, energy, E

# hjelpemetode for å gjøre koden mer ryddig når vi beregner lilleSigma_1 --> lilleSigma_4 i RK4 / RK45
def sigma(I, W, L, h, exp_inp):
    """
    :param Sigma: forrige sigma som ble beregnet
    :param h: steglengden
    :param I: treghetsmomentet
    :param W: tilnærming av punktene i løsningen sålangt
    :param L: dreiemomentet
    :return: neste Sigma verdi som brukes i RK metodene
    """
    return np.dot(np.linalg.inv(I), np.dot(exp(-h, exp_inp), np.dot(W.T, L)))


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.double)
    h = get_h()
    interval = [0, 2]
    n = 10000
    L = np.array([1, 0, 0], dtype=np.double)
    I = np.identity(3, dtype=np.double)
    W_r, t, _, E = RK45(X_0, interval, n, L, I)
    print(W_r[-1])
    print(exactSolution([2]))
