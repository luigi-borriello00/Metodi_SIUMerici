# -*- coding: utf-8 -*-
"""
Newton Modificato
"""

import iterazione as it
import sympy as sym
import sympy.utilities.lambdify
import allMethods as fz
import numpy as np
import matplotlib.pyplot as plt

x = sym.symbols('x')

# Preparo i dati
fx1 = sym.exp(-x) - (x + 1)
dfx1 = sym.diff(fx1, x, 1)

fx2 = sym.log(x+3, 2) - 2
dfx2 = sym.diff(fx2, x, 1)

fx3 = sym.sqrt(x) - (x**2) / 4
dfx3 = sym.diff(fx3, x, 1)

# Trasformo in numeriche
f1 = sym.lambdify(x, fx1, np)
df1 = sym.lambdify(x, dfx1, np)

f2 = sym.lambdify(x, fx2, np)
df2 = sym.lambdify(x, dfx2, np)

f3 = sym.lambdify(x, fx3, np)
df3 = sym.lambdify(x, dfx3, np)

# Inizio a calcolare
# Bisezione
x1Bis, it1Bis, xk1Bis = fz.bisezione(f1, -1, 2, 1.e-12)
x2Bis, it2Bis, xk2Bis = fz.bisezione(f2, -1, 2, 1.e-12)
x3Bis, it3Bis, xk3Bis = fz.bisezione(f3, 1, 3, 1.e-12)

# Falsi
x1Fals, it1Fals, xk1Fals = fz.regula_falsi(f1, -1, 2, 1.e-12, 500)
x2Fals, it2Fals, xk2Fals = fz.regula_falsi(f2, -1, 2, 1.e-12, 500)
x3Fals, it3Fals, xk3Fals = fz.regula_falsi(f3, 1, 3, 1.e-12, 500)

# Corde
x1Cord, it1Cord, xk1Cord = fz.corde(f1, df1, -0.5, 1.e-12, 1.e-12, 500)
x2Cord, it2Cord, xk2Cord = fz.corde(f2, df2, -0.5, 1.e-12, 1.e-12, 500)
x3Cord, it3Cord, xk3Cord = fz.corde(f3, df3, 1.8, 1.e-12, 1.e-12, 500)

# Newton
x1New, it1New, xk1New = fz.newton(f1, df1, -0.5, 1.e-12, 1.e-12, 500)
x2New, it2New, xk2New = fz.newton(f2, df2, -0.5, 1.e-12, 1.e-12, 500)
x3New, it3New, xk3New = fz.newton(f3, df3, 1.8, 1.e-12, 1.e-12, 500)

# Secanti
x1Sec, it1Sec, xk1Sec = fz.secanti(f1, -0.5, -0.3, 1.e-12, 1.e-12, 500)
x2Sec, it2Sec, xk2Sec = fz.secanti(f2, -0.5, -0.3, 1.e-12, 1.e-12, 500)
x3Sec, it3Sec, xk3Sec = fz.secanti(f3, 1.8, 1.5, 1.e-12, 1.e-12, 500)

e1bis = np.abs(xk1Bis - np.array(0))
e1Falsi = np.abs(xk1Fals - np.array(0))
e1Cord = np.abs(xk1Cord - np.array(0))
e1New = np.abs(xk1New - np.array(0))
e1Sec = np.abs(xk1Sec - np.array(0))

e2bis = np.abs(xk2Bis - np.array(0))
e2Falsi = np.abs(xk2Fals - np.array(0))
e2Cord = np.abs(xk2Cord - np.array(0))
e2New = np.abs(xk2New - np.array(0))
e2Sec = np.abs(xk2Sec - np.array(0))

e3bis = np.abs(xk3Bis - np.array(0))
e3Falsi = np.abs(xk3Fals - np.array(0))
e3Cord = np.abs(xk3Cord - np.array(0))
e3New = np.abs(xk3New - np.array(0))
e3Sec = np.abs(xk3Sec - np.array(0))

plt.semilogy(np.arange(it1Bis-1), e1bis, "-go", np.arange(it1Fals-1), e1Falsi, "-ro")
plt.legend(["Bisezione", "Secanti"])
plt.show()