# -*- coding: utf-8 -*-
"""
ITERAZIONE pto fisso

NO controllo su residuo

"""

def iterazione(gfunc, x0, tol, nMax):
    xk = []
    xk.append(x0)
    x1 = gfunc(x0)
    xk.append(x1)
    it = 1
    err = x1 - x0
    while it < nMax and abs(err) >= tol * abs(x1):
        x0 = x1
        x1 = gfunc(x0)
        xk.append(x1)
        it += 1
        err = x1 - x0
        if it == nMax:
            print("Raggiunto n° max di iterazioni")
    return x1, it, xk