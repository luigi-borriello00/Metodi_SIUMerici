# -*- coding: utf-8 -*-
"""
Metodo di Newton

Differenza: Ogni incremento va moltiplicato per m
"""

def newtonModificato(func, dfunc, x0, tolx, tolf, nMax, m):
    it = 0
    xk = []
    # Controllo Derivata
    if abs(dfunc(x0)) == 0:
        print("Derivata nulla")
        return [], 0, []
    # xi = xim1 - d
    d = func(x0)/dfunc(x0)
    x1 = x0 - (d*m)
    xk.append(x1)
    it += 1
    while it < nMax and abs(func(x1)) >= tolf and abs(d) >= tolx * abs(x1):
        x0 = x1
        # Controllo Derivata
        if abs(dfunc(x0)) == 0:
            print("Derivata nulla")
            return x0, it, xk
        d = func(x0)/dfunc(x0)
        x1 = x0 - (d*m)
        xk.append(x1)
        it += 1
        if it == nMax:
            print("Raggiunto nMax iterazioni")
    return x1, it, xk