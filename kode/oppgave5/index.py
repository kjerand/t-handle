import sys

sys.path.append("..")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
from oppgave1.oppgave1_funksjoner import treghetsmoment, M, L, R, energi, calculate_L
from oppgave4.RK45 import RK45
from oppgave4.RK4 import RK4
from oppgave3.euler import euler
from utils.utils import get_h


def oppgave5(X_0, omega_0, n, interval, drop_energy=False):
    """
    :param X_0: initialverdi til X.
    :param omega_0: vinkelhastighet ved tidspunkt 0
    :param n: antall steg.
    :param interval: start og sluttidspunkt for beregningen
    :param drop_energy: bestemmer hvorvidt vi skal droppe eller ta med energiberegningene
    :return: et tuppel med dictionaries som inneholder informasjon om
             plassering av punktene, timestampene deres, og energien
             ved de ulike tidspunktene for de tre ulike metoden RK4, RK45, Euler.
    """
    I = treghetsmoment(M, R, L)
    L_vector = np.dot(X_0, np.dot(I, omega_0))  # calculate_L(I, omega_0)

    initial_energy = energi(I, omega_0) if not drop_energy else 0

    W_rk45, t_rk45, energy_rk45, E = RK45(X_0, interval, n, L_vector, I, initial_energy)
    W_rk4, t_rk4, energy_rk4, _ = RK4(X_0, interval, n, L_vector, I, initial_energy)
    W_e, t_euler, energy_euler, _ = euler(X_0, interval, n, L_vector, I, initial_energy)

    return (
        {"rk45": W_rk45, "rk4": W_rk4, "euler": W_e},
        {"rk45": t_rk45, "rk4": t_rk4, "euler": t_euler},
        {"rk45": energy_rk45, "rk4": energy_rk4, "euler": energy_euler},
        E,
    )


if __name__ == "__main__":
    n = 5000
    interval = [0.0, 5.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    W_a, t_a, energy_a, E = oppgave5(X_0, omega_0_a, n, interval)
    print(W_a["rk45"][-1])

    omega_0_b = np.array([[0, 1, 0.05]], dtype=np.double).T
    W_b, t_b, energy_b, E = oppgave5(X_0, omega_0_b, n, interval)
    print(W_b["rk45"][-1])

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    W_c, t_c, energy_c, E = oppgave5(X_0, omega_0_c, n, interval)
    print(W_c["rk45"][-1])

    f, (ax1, ax2, ax3) = plt.subplots(1, 3)

    for method in ["euler", "rk4", "rk45"]:
        ax1.plot(t_a[method], energy_a[method], label=f"{method}")
        ax1.set_xlabel("Tid i sekunder")
        ax1.set_ylabel("Energi i mikrojoule")
        ax1.set_title("a)")

    for method in ["euler", "rk4", "rk45"]:
        ax2.plot(t_b[method], energy_b[method], label=f"{method}")
        ax2.set_xlabel("Tid i sekunder")
        ax2.set_ylabel("Energi i mikrojoule")
        ax2.set_title("b)")

    for method in ["euler", "rk4", "rk45"]:
        ax3.plot(t_c[method], energy_c[method], label=f"{method}")
        ax3.set_xlabel("Tid i sekunder")
        ax3.set_ylabel("Energi i mikrojoule")
        ax3.set_title("c)")

    plt.legend()
    plt.show()
