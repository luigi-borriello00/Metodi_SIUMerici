# -*- coding: utf-8 -*-
"""
ese9
"""
import numpy as np
import numpy.linalg as npl
import s
import interpolL as fz
import math
import matplotlib.pyplot as plt

f= lambda x: np.sin(2*math.pi*x)
x=np.linspace(-1,1,22)
y1=f(x);

y2=y1.copy()
y2=y2+0.0002*np.random.randn(22,)

xx = np.linspace(np.min(x), np.max(x), 200)
pol = fz.interpolL(x, y1, xx)
polP = fz.interpolL(x, y2, xx)
errRelDati = np.linalg.norm(y1-y2, 2) / np.linalg.norm(y1)
errRelPol = np.linalg.norm(pol-polP, 2) / np.linalg.norm(pol)
plt.plot(x, y2, "b*", xx, pol, "r", xx, polP, "g", x, y1, "y*")
plt.legend(["Punti di interpolazione", "Polinomio", "Polinomio Perturbato", "Pti perturbati"])
plt.show()
print("Errore Relativo sui dati: ", errRelDati)
print("Errore Relativo sul polinomio: ", errRelPol)