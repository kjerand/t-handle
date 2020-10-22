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


def oppgave(X_0, omega_0, n, interval, drop_energy=False):

    # L_vector = np.array([1.0, 0.0, 0.0])
    I = treghetsmoment(M, R, L)
    L_vector = calculate_L(X_0, I, omega_0)

    initial_energy = energi(X_0, I, omega_0) if not drop_energy else 0

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
    n = 60000
    interval = [0.0, 200.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    # W_a, t_a, energy_a, E = oppgave(X_0, omega_0_a, n, interval, drop_energy=True)

    omega_0_b = np.array([[0, 1, 0.05]], dtype=np.double).T
    W_b, t_b, energy_b, E = oppgave(X_0, omega_0_b, n, interval)

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    W_c, t_c, energy_c, E = oppgave(X_0, omega_0_c, n, interval)

    # Kan ikke se rk4 pga. fullstendig overlapp med rk45.
    while True:
        oppgave = input("Oppgave nr [a, b, c]: ")
        if oppgave == "a":
            for method in ["euler", "rk4", "rk45"]:
                plt.plot(t_a[method], energy_a[method], label=f"{method}")
            plt.legend()
            plt.show()
        if oppgave == "b":
            for method in ["euler", "rk4", "rk45"]:
                plt.plot(t_b[method], energy_b[method], label=f"{method}")
            plt.legend()
            plt.show()
        if oppgave == "c":
            for method in ["euler", "rk4", "rk45"]:
                plt.plot(t_c[method], energy_c[method], label=f"{method}")
            plt.legend()
            plt.show()
