import sys

sys.path.append("..")

import numpy as np
from oppgave1.oppgave1_funksjoner import exp
from oppgave3.euler import euler
from utils.utils import get_h, big, A, B, c

def RK45(X_0, h, n, L, I):
    W = [X_0]

    for i in range(0, n):
        sigma1 = np.dot(np.linalg.inv(I), np.dot(W[i], L))
        sigma2 = sigma(I, W[i], L, h, A[convert_index(2, 1)]*big(sigma1))
        sigma3 = sigma(I, W, L, h, A[2, 0])
        sigma4 = sigma(I, W, L, h, A[4, ])

def sigma(I, W, L, h, exp_inp):
    return np.dot(np.linalg.inv(I), np.dot(exp(-h, exp_inp), np.dot(W.T, L)))