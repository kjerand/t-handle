import sys

sys.path.append("..")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
from oppgave1.oppgave1_funksjoner import treghetsmoment, M, L, R
from oppgave4.RK45 import RK45
from utils.utils import get_h


def oppgave(X_0, omega_0, n, interval):
    L_vector = calculate_L(X_0, omega_0)

    I = treghetsmoment(M, R, L)

    return RK45(X_0, interval, n, L_vector, I)


def calculate_L(X, omega):
    return np.dot(X, np.dot(np.identity(3, dtype=np.double), omega))


def draw(W, ax):
    ax.clear()
    size = 1.0
    ax.scatter(
        [
            1.0 * size,
            1.0 * size,
            1.0 * size,
            1.0 * size,
            -1.0 * size,
            -1.0 * size,
            -1.0 * size,
            -1.0 * size,
        ],
        [
            1.0 * size,
            -1.0 * size,
            1.0 * size,
            -1.0 * size,
            1.0 * size,
            -1.0 * size,
            1.0 * size,
            -1.0 * size,
        ],
        [
            -1.0 * size,
            -1.0 * size,
            1.0 * size,
            1.0 * size,
            -1.0 * size,
            -1.0 * size,
            1.0 * size,
            1.0 * size,
        ],
        s=1,
    )
    ax.scatter([i[0] for i in W.T], [i[1] for i in W.T], [i[2] for i in W.T])


if __name__ == "__main__":
    n = 5000
    interval = [0.0, 2000.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    W_a, t, E = oppgave(X_0, omega_0_a, n, interval)

    omega_0_b = np.array([[0, 1, 0.05]], dtype=np.double).T
    W_b, t, E = oppgave(X_0, omega_0_b, n, interval)

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    W_c, t, E = oppgave(X_0, omega_0_c, n, interval)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    axTime = plt.axes([0.2, 0.1, 0.65, 0.03])
    sTime = Slider(
        axTime,
        "Time",
        interval[0],
        interval[1],
        valinit=interval[0],
        valstep=float((interval[1] - interval[0]) / n),
    )

    sTime.on_changed(
        lambda val: draw(
            W_c[int(((val / (interval[1] - interval[0])) * n) - interval[0])], ax
        )
    )

    ax.scatter([i[0] for i in W_c[0]], [i[1] for i in W_c[0]], [i[2] for i in W_c[0]])

    plt.show()
