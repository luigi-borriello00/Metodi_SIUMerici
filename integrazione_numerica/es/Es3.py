# -*- coding: utf-8 -*-
"""
Es 3
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import allM as fz
import math
import Funzioni_Integrazione as fzz

scelta = input("Seleziona integrale ")
x = sym.Symbol("x")
alpha = np.array([13./2., 5./2., 1./2.])
integrali = {
    "1" : [sym.cos(x), 0., 2.],
    "2" : [x * sym.exp(x) * sym.cos(x**2), 2 * -math.pi, 0],
    "3" : [sym.Pow(sym.sin(x), alpha[0]), 0, math.pi/2],
    "4" : [sym.Pow(sym.sin(x), alpha[1]), 0, math.pi/2],
    "5" : [sym.Pow(sym.sin(x), alpha[2]), 0, math.pi/2]
        }
fx, a, b = integrali.get(scelta)
Iesatto = float(sym.integrate(fx, (x,a,b)))
f = sym.utilities.lambdify(x, fx, np)
errRelT = []
errRelS = []
nIntT = []
nIntS = []
kT = []
kS = []
nValT = []
nValS = []
for k in range(4, 11):
    print(k)
    tol = (10.0 ** (-k))
    It, Nt = fz.trapTol(f, a, b, tol)
    Is, Ns = fz.simpTol(f, a, b, tol)
    if Nt > 0:
        nIntT.append(Nt)
        errRelT.append(abs(It - Iesatto) / abs(Iesatto))
        kT.append(k)
        nValT.append(Nt + 1)
    if Ns > 0:
        nIntS.append(Ns)
        errRelS.append(abs(Is - Iesatto) / abs(Iesatto))
        kS.append(k)
        nValS.append(2 * Ns + 1)
plt.semilogy(kT, errRelT, "b-o", kS, errRelS, "r-*")
plt.legend(["ErrRelTrap", "ErrRelSimp"])
plt.show()
plt.plot(kT, nIntT, "b-o", kS, nIntS, "r-*")
plt.legend(["NSottIntTrap", "NSottIntSimp"])
plt.show()
plt.plot(kT, nValT, "b-o", kS, nValS, "r-*")
plt.legend(["NValTrap", "NValSimp"])
plt.show()