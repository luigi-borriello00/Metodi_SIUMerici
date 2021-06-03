# -*- coding: utf-8 -*-
"""
Secanti sium

Controllo su:
    - nIter
    - Residuo
    - ErrRel 
"""

def secanti(fname, x0, xm1, tolx, tolf, nMaxIt):
    xk = []
    it = 0
    m = (fname(x0) - fname(xm1)) / (x0 - xm1)
    d = fname(x0) / m
    xk.append(x0 - d)
    it += 1
    while it < nMaxIt and abs(fname(x0-d)) >= tolf and abs(d) >= tolx * abs(x0 - d):
        xm1 = x0
        x0 = x0 - d
        m = (fname(x0) - fname(xm1)) / (x0 - xm1)
        d = fname(x0) / m
        xk.append(x0 - d)
        it += 1
        if it == nMaxIt:
            print("Numero massimo it raggiunte ")
            return xk[it-1], it, xk