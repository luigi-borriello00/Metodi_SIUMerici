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

def traptoll(fun, a, b, tol):
    Nmax = 2048
    err = 1
    N = 1;
    IN = trapComposita(fun, a, b, N);
    while N <= Nmax and err > tol :
        N = 2 * N
        I2N = trapComposita(fun, a, b, N)
        err = abs(IN - I2N) / 3
        IN = I2N
    if N > Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        N = 0
        IN = []
    return IN,N