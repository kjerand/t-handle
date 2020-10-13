import sys

sys.path.append("..")

from pylab import plot, show
import numpy as np
from oppgave1.oppgave1_funksjoner import treghetsmoment, M, L, R
from oppgave4.RK45 import RK45
from utils.utils import get_h


def oppgave(omega_0, n, interval):

    X_0 = np.identity(3, dtype=np.double)

    L_vector = calculate_L(X_0, omega_0)

    I = treghetsmoment(M, R, L)

    return RK45(X_0, interval, n, L_vector, I)


def calculate_L(X, omega):
    return np.dot(X, np.dot(np.identity(3, dtype=np.double), omega))


if __name__ == "__main__":
    n = 1000
    interval = [0.0, 100.0]

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    W_a, t, E = oppgave(omega_0_a, n, interval)

    omega_0_b = np.array([[0, 1, 0.05]], dtype=np.double).T
    W_b, t, E = oppgave(omega_0_b, n, interval)

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    W_c, t, E = oppgave(omega_0_c, n, interval)

    print(W_a[n - 1].shape)
