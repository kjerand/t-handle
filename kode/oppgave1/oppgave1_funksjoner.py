#  Oppgave 1.a)

import sys

sys.path.append("..")
import numpy as np
from utils.utils import get_h

# Konstanter for indeksering
x = 0
y = 1
z = 2

# Informasjon om håndtaket
M_1 = 8.0 * np.pi  # g
L_1 = 8.0  # meter
R_1 = 1.0  # meter

# Informasjon om sylinderen festet på håndtaket
M_2 = 4.0 * np.pi  # kg
L_2 = 4.0  # meter
R_2 = 1.0  # meter

M = np.array([M_1, M_2], dtype=np.double)
R = np.array([R_1, R_2], dtype=np.double)
L = np.array([L_1, L_2], dtype=np.double)


def exp(h, Omega):
    """
    :param h: steglengde
    :param Omega: TODO: skrive hva omega er AKKURAT HER!
    """
    I = np.identity(3, dtype=np.double)
    omega = np.sqrt(Omega[2, 1] ** 2 + Omega[0, 2] ** 2 + Omega[1, 0] ** 1)

    return (
        I
        + np.dot((1 - np.cos(h * omega)), np.square(Omega) / (omega ** 2))
        + np.dot(np.sin(h * omega), Omega / omega)
    )


def energi(X, I, omega):
    """
    :param X: rotasjon
    :param I: treghetsmoment
    :param omega: vinkelhastighetsvektor
    """

    L = calculate_L(X, I, omega)

    return (1 / 2) * np.abs(np.vdot((L), omega))


def calculate_L(X, I, omega):
    return np.dot(np.dot(X, I), omega)


def treghetsmoment(M, R, L):
    """
    :param M: Massen til de to sylinderne
    :param R: Radiusen til de to sylinderne
    :param L: lengden til de to sylinderne
    """
    I = np.full((3, 3), 0, dtype=np.double)
    I[x, x] = (M[0] * R[0] ** 2) / 4 + (M[0] * L[0] ** 2) / 12 + (M[1] * R[1] ** 2) / 2

    I[y, y] = (
        M[0] * (R[0] ** 2)
        + (M[1] * L[1]) / 4
        + (M[0] * R[0] ** 2) / 2
        + (M[1] * R[1] ** 2) / 4
        + (M[1] * L[1] ** 2) / 12
    )

    I[z, z] = (
        M[0] * (R[0] ** 2)
        + ((M[1] * L[1]) / 4)
        + ((M[0] * (R[0] ** 2)) / 4)
        + ((M[0] * (L[0] ** 2)) / 12)
        + ((M[1] * (R[1]) ** 2) / 4)
        + ((M[1] * (L[1] ** 2)) / 12)
    )

    return I


def oppgaveA():
    print("Oppgave 1.a)")
    print("Starter tester...")

    # Tester er en liste med testdata vi bruker for å verifisere at kodens numeriske løsning er tilfredsstillende
    tester = [
        {"x": 3, "y": 2, "z": 1},
        {"x": 1, "y": 1, "z": 1},
        {"x": 100, "y": -100, "z": 50},
        {"x": -3, "y": -2, "z": -1},
        {
            "x": -3.14159265358979323846433832795028841971693993,
            "y": 2.718281828459045,
            "z": 1.0,
        },
    ]
    antall_godkjente = 0  # hjelpevariabel for utskrift av tester

    TOL = (
        0.0001  # høyeste feiltoleranse når vi tester at exp(hO)exp(hO)^T == identity(3)
    )

    # her kjører vi alle testene
    for idx, t in enumerate(tester):

        # lager omegamatrisen fra testdataen
        Omega = np.array(
            [
                [0, -t["z"], t["y"]],
                [t["z"], 0, -t["x"]],
                [-t["y"], t["x"], 0],
            ],
            dtype=np.double,
        )

        # kjører funksjonen vår med omega, legger resultatet i X
        h = get_h()
        X = exp(h, Omega)

        # her er eksakt identitetsmatrise og vår tilnærming
        I_approx = np.dot(X, X.T)
        I_eksakt = np.identity(3)

        # største avviket fra identitetsmatrisen i vår tilnærming
        diff = np.absolute(I_eksakt - I_approx)

        # status_godkjent er True dersom den største feilen er mindre enn taket vi bestemte tidligere
        status_godkjent = diff.flatten().max() < TOL
        antall_godkjente += 1 if status_godkjent else 0
        print(
            f"Test {idx+1}: {'bestått' if status_godkjent else 'feilet'}"
        )  # utskrift for oversiktlig kjøring
    print(f"{antall_godkjente}/{len(tester)} tester godkjent\n")


def oppgaveB():
    print("Oppgave 1.b)")
    I = treghetsmoment(M, R, L)
    omega = np.full((3, 1), 2, dtype=np.double)
    K = energi(np.identity(3, dtype=np.double), I, omega)
    print(f"Den kinetiske rotasjonsenergien er {K} J\n")


def oppgaveC():
    print(f"Oppgave 1.c)")
    I = treghetsmoment(M, R, L)
    print(f"Treghetsmomentet til t-nøkkelen er\n {I}")


if __name__ == "__main__":
    oppgaveA()
    oppgaveB()
    oppgaveC()
