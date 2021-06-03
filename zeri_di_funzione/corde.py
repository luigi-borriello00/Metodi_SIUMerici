# -*- coding: utf-8 -*-
"""
Metodo delle corde

Controllo su:
    - nIter
    - Residuo
    - ErrRel
"""

def corde(fname, fpname, x0, tolx, tolf, nMaxIt ):
    xks = []
    it = 0
    m = fpname(x0)
    # decremento costante quindi
    d = fname(x0)/m
    x1 = x0-d
    xks.append(x1)
    it += 1
    while it < nMaxIt and abs(fname(x1)) >= tolf and abs(x1-x0) >= tolx * abs(x1):
        x0 = x1
        x1 = x0-d
        xks.append(x1)
        it += 1
        if it == nMaxIt:
            print("Raggiunto numero massimo di iterazioni")
    return xks[it-1], it, xks