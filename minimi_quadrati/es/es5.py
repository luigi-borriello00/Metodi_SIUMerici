# -*- coding: utf-8 -*-
"""
ese5
"""
import numpy as np
import math 
import funzioni_Interpolazione_Polinomiale as fz
import matplotlib.pyplot as plt

#nodi del problema di interpolazione 
x = np.arange(0,2*math.pi+0.1,math.pi/2);
y1 = np.sin(x)
y2 = np.cos(x)
xx = np.arange(0,2*math.pi+0.1,math.pi/40);

yy1 = fz.interpL(x, y1, xx)
yy2 = fz.interpL(x, y2, xx)

plt.plot(x, y1, "b*", xx, yy1, "r", xx, np.sin(xx), "g")
plt.legend(["Pti di interpolazione", "Polinomio Lagrange", "Funzione"])
plt.title("Sen(x)")
plt.show()

plt.plot(x, y2, "b*", xx, yy2, "r", xx, np.cos(xx), "g")
plt.legend(["Pti di interpolazione", "Polinomio Lagrange", "Funzione"])
plt.title("Cos(x)")
plt.show()