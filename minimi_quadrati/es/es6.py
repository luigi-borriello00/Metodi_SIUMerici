# -*- coding: utf-8 -*-
"""
ese6
"""


import numpy as np
import funzioni_Interpolazione_Polinomiale as fz
import matplotlib.pyplot as plt

#nodi del problema di interpolazione 

L = np.array([-55, -45, -35, -25, -15, -5, 5, 15, 25, 35, 45, 55, 65])
T = np.array([3.7, 3.7,3.52,3.27, 3.2, 3.15, 3.15, 3.25, 3.47, 3.52, 3.65, 3.67, 3.52])

# punti di valutazione per l'interpolante
xx=np.linspace(np.min(L),np.max(L),200);
pol = fz.interpL(L, T, xx)
temp = np.array([-42, +42])
yTemp = fz.interpL(L, T, temp)

plt.plot(L, T, "b*", xx, pol, "r", temp, yTemp, "go")
plt.legend(["Dati", "Polinomio di approssimazione", "Stima di L = +- 42"])
plt.show()

