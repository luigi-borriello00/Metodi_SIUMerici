# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:34:21 2021

@author: Luigi
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import scipy as sci
from scipy.optimize import fsolve
import sympy as sym

def puntofisso(g, x0, tol, nMax):
    xks = []
    xks.append(x0)
    x1 = g(x0)
    xks.append(x1)
    it = 1
    while it < nMax and abs(x1 - x0) >= tol * abs(x1):
        x0 = x1
        x1 = g(x0)
        xks.append(x1)
        it += 1
    return x1, it, xks

def ordine(xks, iteraz):
    num = math.log(abs(xks[iteraz - 1] - xks[iteraz - 2]) / abs(xks[iteraz - 3] - xks[iteraz - 2]))
    den = math.log(abs(xks[iteraz - 3] - xks[iteraz - 2]) / abs(xks[iteraz - 3] - xks[iteraz - 4]))
    return num / den

x = sym.Symbol("x")
gx = sym.tan((3/2) * x) - 2 * sym.cos(x) - x * (6 - x)
g = sym.utilities.lambdify(x, gx, np)
dgx = sym.diff(gx, x, 1)
dg = sym.utilities.lambdify(x, dgx, np)

# Plotto la funzione per cercare zeri
xx = np.linspace(-1, 1, 100)
plt.plot(xx, xx, xx, g(xx))
plt.show()

radice = fsolve(g, -1)


print(radice)
"""
La |derivata| è < 1 in un intorno quindi rispetta il th di convergenza locale
"""
xrad = np.linspace(radice - 0.1, radice + 0.1, 100)


plt.plot(xrad, abs(dg(xrad)), xrad, np.zeros(100,))
plt.show()


geqx = (sym.tan((3/2) * x) - 2 * sym.cos(x)) / (6 - x)
geq = sym.utilities.lambdify(x, geqx, np)
dgeqx = sym.diff(geqx, x, 1)
dgeq = sym.utilities.lambdify(x, dgeqx, np)
plt.plot(xx, xx, xx, geq(xx))
plt.show()
radice = fsolve(geq, -0.20)

print(abs(dgeq(radice)))
plt.plot(xrad, abs(dgeq(xrad)), xrad, np.zeros(100,))
plt.show()

# Testo puntofisso

x0 = 0
tol = 1.e-7
nmax = 500

x1, iteraz, xks = puntofisso(g, x0, tol, nmax)
plt.plot(np.arange(iteraz + 1), xks)
print(ordine(xks, iteraz + 1))

