# -*- coding: utf-8 -*-
"""
Es 2
"""

import allMethods as fz
import math
import sympy as sym
import sympy.utilities.lambdify
import numpy as np
import matplotlib.pyplot as plt

x = sym.symbols("x")
fx = sym.tan(x) - x
dfx = sym.diff(fx, x, 1)
f = sym.lambdify(x, fx, np)
df = sym.lambdify(x, dfx, np)

x, iterazioni, xks = fz.bisezione(f, (3/5)*math.pi, (37/25)*math.pi, 1e-8)
for x in range(4):
    xNew, itNew, xkNew = fz.newton(f, df, xks[x], 1e-8, 1e-8, 200)
    xSec, itSec, xkSec = fz.secanti(f, xks[x], (3/5)*math.pi, 1e-8, 1e-8, 200)
    print("valore: {:e}, Newton xk={:e} con {:d} iterazioni".format(xks[x], xNew, itNew))
    print("valore: {:e}, Secanti xk={:e} con {:d} iterazioni".format(xks[x], xSec, itSec))
