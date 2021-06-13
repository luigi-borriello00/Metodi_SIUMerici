# -*- coding: utf-8 -*-
"""
Formule di Simpson
"""
import numpy as np

"""
    Simpson Composita
    se n = 1 -> Simpson semplice
"""
def simpComposita(fname, a, b, n):
    h = (b - a) / (2 * n)
    nodi = np.arange(a, b + h, h)
    f = fname(nodi)
    # f nel primo segmento + 2 volte f calcolata nei pari + 4 f calcolata nei dispari
    I = (f[0] + 2 * np.sum(f[2 : 2 * n : 2]) + 4 * np.sum(f[1 : 2 * n : 2]) + f[2 * n]) * h / 3
    return I

"""
    Quadratura automatica
"""
def simpTol(fname, a, b, tol):
    err = 1
    N = 1
    In = simpComposita(fname, a, b, N)
    NMAX = 2048
    while N <= NMAX and err > tol:
        N = N * 2
        I2n = simpComposita(fname, a, b, N)
        err = abs(In - I2n) / 15
        In = I2n
    if N > NMAX:
        print("Raggiunto numero massimo di iterazioni")
        N = 0
        IN = []
        return IN, N
    return In, N