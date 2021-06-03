# -*- coding: utf-8 -*-
"""
Regula Falsi

Controllo su:
    - nIter
    - Residuo
    - Intervallo con tolleranza + eps * max(a,b)
"""
import numpy as np
import math

def sign(x) : return math.copysign(1, x)

def regula_falsi(fname, a, b, tol, nMax):
    # A e B devono avere segni discordi
    if sign(fname(a)) == sign(fname(b)):
        print("Algoritmo non applicabile")
        return [], 0, []
    else:
        xks = []
        it = 0
        eps = np.spacing(1)
        while it < nMax and abs(b-a) >= tol + eps * max(abs(a), abs(b)) and fname(xks[it]) >= tol:
            # Calcolo il nuovo punto Xk
            xks.append(a - fname(a) * ((b - a)/(fname(b) - fname(a))))
            if math.copysign(1, xks[it]) == math.copysign(1,a):
                a = xks[it]
            elif math.copysign(1, xks[it]) == math.copysign(1,b):
                b = xks[it]
            elif fname(xks[it]) == 0:
                break;
            it += 1
        return xks[it], it+1, xks