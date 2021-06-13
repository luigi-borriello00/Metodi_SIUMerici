# -*- coding: utf-8 -*-
"""
Formule Trapezi
"""
import numpy as np

"""
    Trapezi Composita
    se n = 1 -> Trapezi Semplice
"""
def trapComposita(fname, a, b, n):
    h = (b - a) / n
    nodi = np.arange(a, b + h, h)
    f = fname(nodi)
    I = (f[0] + 2 * np.sum(f[1 : n]) + f[n]) * h / 2
    return I

"""
    Quadratura automatica
"""
def trapTol(fname, a, b, tol):
    NMAX = 2048
    err = 1
    N = 1
    IN = trapComposita(fname, a, b, N)
    while N <= NMAX and err > tol:
        N = N * 2
        I2N = trapComposita(fname, a, b, N)
        err = abs(IN - I2N) / 3
        IN = I2N
    if N > NMAX:
        print("Raggiunto numero massimo di iterazioni")
        N = 0
        IN = []
        return IN, N
    return IN, N