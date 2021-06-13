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
    I = (f[0] + 2 * np.sum(f[2 : 2 * n : 2]) + 4 * np.sum(f[1 : 2 * n : 2]) + f[2 * n]) * h / 3
    return I

def simptoll(fun, a, b, tol):
    Nmax = 2048
    err = 1    
    N = 1;
    IN = simpComposita(fun, a, b, N);
    while N <= Nmax and err > tol:
        N = 2 * N
        I2N = simpComposita(fun, a, b, N)
        err = abs(IN - I2N) / 15
        IN = I2N
    if N > Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        N = 0
        IN = []
    return IN,N