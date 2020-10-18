import sys

sys.path.append("..")

import numpy as np
from tqdm import tqdm
from oppgave1.oppgave1_funksjoner import exp, energi
from oppgave3.euler import euler
from oppgave4.RK4 import RK4
from utils.utils import get_h, big, A, B, c, max_energy_difference
from tqdm import tqdm


def RK45(X_0, interval, n, L, I, omega):
    h = float((interval[1] - interval[0]) / n)
    t = [i * h for i in range(n + 1)]
    W = [X_0]
    Z = [X_0]
    E = [0]

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
        """
        if np.abs(energi(W[-1], I, omega)-energi(W[0], I, omega)) > max_energy_difference :
            print(energi(W[-1], I, omega))
            print(energi(W[0], I, omega))
            print("\n")
            return RK45(X_0, interval, n*2, L, I, omega)
        """

        Z.append(
            np.dot(
                W[i],
                exp(h, sum(B[1, i] * big(sigmas[i]) for i in range(6))),
            ),
        )

        deltaW = W[i + 1] - Z[i + 1]
        E.append(np.sqrt(np.trace(np.dot(deltaW.T, deltaW))))

    return W, t, E


def sigma(I, W, L, h, exp_inp):
    return np.dot(np.linalg.inv(I), np.dot(exp(-h, exp_inp), np.dot(W.T, L)))


if __name__ == "__main__":
    X_0 = np.identity(3, dtype=np.double)
    h = get_h()
    interval = [0, 10]
    n = 100
    L = np.array([1, 0, 0], dtype=np.double)
    I = np.identity(3, dtype=np.double)
    W_r, t, E = RK45(X_0, [0.0, 10.0], n, L, I)
    W_e = euler(X_0, h, n, L, I)
    W_r4 = RK4(X_0, h, n, L, I)

    print(W_e[n], end="\n\n")
    print(W_r4[n], end="\n\n")
    print(W_r[n])