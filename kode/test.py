"""
Her bør det skrives litt om hva som er hensikten med denne fila.
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

"""
Her er et eksempel på hvordan vi bør definere konstanter. Den skal ha store bokstaver,
og skal ikke endre verdi gjennom kodens livsløp.
"""
CONSTANT = 2

"""
Her har vi et eksempel på en funksjon som er kommentert på en god måte.
"""
def sum(a, b, c):
    """
    :param a: Første heltall. 
    :param b: Andre heltall.
    :param c: Tredje heltall.
    :return: Summen av heltallene (a+b+c)
    """
    return a + b + c

## All kode som ikke er en funksjon/klasse/konstant skal bare være i "main":
if __name__ == "__main__":
    a, b, c = [int(x) for x in input("Skriv inn 3 heltall separert med mellomrom: ").split()]
    print(f"{a} + {b} + {c} = {sum(a, b, c)}") # Bruk f-strings istedenfor format.