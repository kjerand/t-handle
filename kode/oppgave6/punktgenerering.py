import sys

sys.path.append("..")

from oppgave5.index import oppgave
from utils.utils import get_h

import numpy as np
import pickle


def save_data(X_0, omega_0, n, interval, filename, drop_energy=False):
    W, t, _, E = oppgave(X_0, omega_0, n, interval, drop_energy=drop_energy)
    pickle.dump([W, t, E], open(f"data/{filename}", "wb"))


def load_data(filename):
    data = pickle.load(open(f"data/{filename}", "rb"))
    return (
        np.array(data[0]["rk45"], dtype=np.double),
        np.array(data[0]["rk4"], dtype=np.double),
        np.array(data[0]["euler"], dtype=np.double),
        np.array(data[1]["rk45"], dtype=np.double),
        np.array(data[1]["rk4"], dtype=np.double),
        np.array(data[1]["euler"], dtype=np.double),
        np.array(data[2], dtype=np.double),
    )


if __name__ == "__main__":
    n = 60000
    interval = [0.0, 200.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    save_data(X_0, omega_0_a, n, interval, "testa.npy", drop_energy=True)

    omega_0_b = np.array([[0, 1.0, 0.05]], dtype=np.double).T
    save_data(X_0, omega_0_b, n, interval, "testb.npy")

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    save_data(X_0, omega_0_c, n, interval, "testc.npy")