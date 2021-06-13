# -*- coding: utf-8 -*-
"""
Es 1

"""

import allM as fz
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sym.Symbol("x")

scelta = input("Scegli funzione ")
funzioni = {
    "1" : x**10,
    "2" : sym.log(x + 1),
    "3" : sym.asin(x)
    }
fx = funzioni.get(scelta)
f = sym.utilities.lambdify(x, fx, np)
I = sym.integrate(fx,(x, 0, 1))
errRelS = []
errRelT = []
for n in range(1, 9):
    N = 2**n
    Is = fz.simpsonComp(f, 0, 1, N)
    It = fz.trapeziComp(f, 0, 1, N)
    errRelS.append(abs(I - Is) / abs(I))
    errRelT.append(abs(I - It) / abs(I))
plt.semilogy(2 ** np.arange(1,9), errRelS, "b-*", 2 ** np.arange(1,9), errRelT, "ro-")
plt.legend(["ErrRelSimpson", "ErrRelTrapezi"])
plt.ylabel("ErrRelativo")
plt.xlabel("N sottointervalli")
plt.show()