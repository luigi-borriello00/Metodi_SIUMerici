# -*- coding: utf-8 -*-
"""
Es 6
"""

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import math

def ordine(xks, it):
    num = math.log((abs(xks[it - 1] - xks[it - 2])) / abs(xks[it - 3] - xks[it - 2]))
    den = math.log((abs(xks[it - 3] - xks[it - 2])) / abs(xks[it - 3] - xks[it - 4]))
    return num / den

x = sym.Symbol("x")
fx = x**3 + (4 * (x**2)) - 10

f = sym.utilities.lambdify(x, fx, np)
x0 = 1.5
tol = 1.e-7
nMax = 1000

xx = np.linspace(0, 5, 100)
fxx = f(xx)
plt.plot(xx, fxx, xx, np.zeros((100, )))
radice = sci.optimize.fsolve(f, 1.5)
print(radice)

scelta = input("Scegli funzione ")
gs = {
      "1" : 0.5 * sym.sqrt((- x ** 3) + 10),
      "2" : (x + 10) / ((x**2) + 4*x + 1),
      "3" : sym.sqrt(10 / (x+4))
      }
gx = gs.get(scelta)
print(gx)
dgx = sym.diff(gx, x, 1)
dg = sym.utilities.lambdify(x, dgx, np)
derivata = dg(radice)
print("Derivata != 0 -> p = 1")
ordine = abs(dg(radice))
print(ordine)
