# -*- coding: utf-8 -*-
"""
Simulazione 8 Settembre 2020

Funzione e radici
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy import optimize 
import math


# L'unico metodo a convergenza quadratica è Newton

def newton(fname, fpname, x0, m,  tol, nMaxIt):
    xk = []
    it = 0
    if abs(fpname(x0)) <= np.spacing(1):
        print("Derivata nulla in x0")
        return [], 0, []
    else:
        d = (fname(x0)/ fpname(x0))
        x1 = x0 - d*m
        xk.append(x1)
        it += 1
        while it < nMaxIt and abs(fname(x1)) >= tol and abs(d) >= tol * abs(x1):
            x0 = x1
            if abs(fpname(x0)) <= np.spacing(1):
                print("Derivata nulla in x0")
                return x1, it, xk
            d = (fname(x0)/ fpname(x0))
            x1 = x0 - d*m
            xk.append(x1)
            it += 1
            
        if it == nMaxIt:
            print("Numero massimo di iterazioni raggiunto")
        return x1, it, xk

# Definisco Funzione e derivata 
x = sym.Symbol("x")
xx = np.linspace(1, 3, 100)
fx = x - (2 * sym.sqrt(x - 1))
dfx = sym.diff(fx, x, 1)

f = sym.utilities.lambdify(x, fx, np)
d = sym.utilities.lambdify(x, dfx, np)

# Plotto la funzione per cercare le radici
plt.plot(xx, f(xx))
plt.show()

# Noto che la funzione vicino al 2 vale 0
zero = optimize.fsolve(f, 2.0)
print(zero)

x1, it, xks = newton(f, d, 3.0, 2.0, 1.e-12, 500)
print("La derivata nel punto è ", d(x1))
# Stimo l'ordine di convergenza del metodo
numO = math.log(abs(xks[-2] - xks[-1]) / abs(xks[-3] - xks[-2]))
denO = math.log(abs(xks[-3] - xks[-2]) / abs(xks[-4] - xks[-3]))
ordine = numO / denO
print(f"L'ordine di convergenza del metodo è {ordine}")

# Notiamo che l'ordine è vicino all'uno quindi ziopera ha molteplicità m


plt.plot(xx, d(xx))
plt.title("Derivata")
plt.show()

plt.semilogy(np.arange(it), xks)
plt.title("Iterazioni")
plt.show()