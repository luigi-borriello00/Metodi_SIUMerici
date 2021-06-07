# -*- coding: utf-8 -*-
"""
ese3
"""
import numpy as np
import matplotlib.pyplot as plt
from funzioni_Approssimazione_MQ import metodoQR

x = np.arange(10.0,10.6,0.1)
y = np.array([11.0320, 11.1263, 11.1339, 11.1339, 11.1993, 11.1844])
a1 = metodoQR(x,y,4)
valori = np.linspace(np.min(x), np.max(x), 100)
p1 = np.polyval(a1, valori)
residuo = np.linalg.norm(y - np.polyval(a1, x))**2
print("Residuo: {:e}".format(residuo))
plt.plot(valori, p1, "-r", x, y, "ob")

plt.show()
# Perturbo
x[1] += 0.013
y[1] -= 0.001
a2 = metodoQR(x,y,4)
valori = np.linspace(np.min(x), np.max(x), 100)
p2 = np.polyval(a2, valori)
plt.plot(valori, p2, "-r", x, y, "ob")
residuo = np.linalg.norm(y - np.polyval(a2, x))**2
print("Residuo dati perturbati: {:e}".format(residuo))
plt.show()