import sys

sys.path.append("..")

from oppgave5.index import oppgave
from utils.utils import get_h

import numpy as np
import pickle


def save_data(X_0, omega_0, n, interval, filename):
    W_c, t, E = oppgave(X_0, omega_0, n, interval)
    pickle.dump([W_c, t, E], open(f"data/{filename}", "wb"))


def load_data(filename):
    data = pickle.load(open(f"data/{filename}", "rb"))
    return (
        np.array(data[0], dtype=np.double),
        np.array(data[1], dtype=np.double),
        np.array(data[2], dtype=np.double),
    )


if __name__ == "__main__":
    n = 50000
    interval = [0.0, 2000.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    save_data(X_0, omega_0_a, n, interval, "big.npy")