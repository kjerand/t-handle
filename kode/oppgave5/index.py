import sys

sys.path.append("..")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
from oppgave1.oppgave1_funksjoner import treghetsmoment, M, L, R, energi
from oppgave4.RK45 import RK45
from oppgave4.RK4 import RK4
from oppgave3.euler import euler
from utils.utils import get_h


def oppgave(X_0, omega_0, n, interval):

    # L_vector = np.array([1.0, 0.0, 0.0])
    I = treghetsmoment(M, R, L)
    L_vector = calculate_L(X_0, I, omega_0)

    W_rk45, t, E = RK45(X_0, interval, n, L_vector, I, omega_0)
    W_rk4, _, _ = RK4(X_0, interval, n, L_vector, I)
    W_e, _, _ = euler(X_0, interval, n, L_vector, I)

    print(
        "Lengde: ",
        np.linalg.norm(np.dot(np.linalg.inv(np.dot(X_0, I)), L_vector)),
    )

    return {"rk45": W_rk45, "rk4": W_rk4, "euler": W_e}, t, E


def calculate_L(X, I, omega):
    return np.dot(np.dot(X, I), omega)


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
    interval = [0.0, 10.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    W_a, t, E = oppgave(X_0, omega_0_a, n, interval)
    W_a = W_a["rk45"]

    omega_0_b = np.array([[0, 1, 0.05]], dtype=np.double).T
    W_b, t, E = oppgave(X_0, omega_0_b, n, interval)
    W_b = W_b["rk45"]

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    W_c, t, E = oppgave(X_0, omega_0_c, n, interval)
    W_c = W_c["rk45"]

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
            W_b[int(((val / (interval[1] - interval[0])) * n) - interval[0])], ax
        )
    )

    ax.scatter([i[0] for i in W_b[0]], [i[1] for i in W_b[0]], [i[2] for i in W_b[0]])

    plt.show()
