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
        fk = fname(a)
        while it < nMax and abs(b-a) >= tol + eps * max(abs(a), abs(b)) and abs(fk) >= tol:
            # Calcolo il nuovo punto Xk
            xk = a - fname(a) * ((b - a)/(fname(b) - fname(a)))
            xks.append(xk)
            fk = fname(xk)
            if sign(xks[it]) == sign(a):
                a = xks[it]
            elif sign(xks[it]) == sign(b):
                b = xks[it]
            elif fname(xks[it]) == 0:
                break;
            it += 1
        return xk, it+1, xks