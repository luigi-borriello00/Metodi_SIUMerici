# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:29:01 2021

@author: Luigi
"""

import allMethods as fz
#import funzioni_zeri as fz
import numpy as np
import sympy as sym
import sympy.utilities.lambdify

x = sym.symbols("x")
fx = x**3 + x**2 - 33*x + 63
dfx = sym.diff(fx, x, 1)

f = sym.lambdify(x, fx, np)
df = sym.lambdify(x, dfx, np)

x0 = 1
tolx = 1e-12
tolf = tolx

xkNew, itNew, xksNew = fz.newton(f, df, x0, tolx, tolf, 500)
xkNewM, itNewM, xksNewM = fz.newtonModificato(f, df, x0, tolx, tolf, 500, 2)


convNewton = fz.stimaOrdine(xksNew, itNew-1)
convMod = fz.stimaOrdine(xksNewM, itNewM-1)

print(f"Newton normale -> {convNewton}")
print(f"Newton modificato -> {convMod}")