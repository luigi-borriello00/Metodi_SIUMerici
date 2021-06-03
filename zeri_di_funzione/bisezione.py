# -*- coding: utf-8 -*-
"""
Metodo di bisezione

Controllo iniziale sull'intervallo' iniziale

Controllo su:
    - nIter
    - abs(Intervallo) con tolleranza di macchina * max(ai,bi)
    
"""
import numpy as np
import math

def sign(x) : return math.copysign(1, x)

def bisezione(fname, a, b, tol):
    fa=fname(a)
    fb=fname(b)
    if sign(fa)==sign(fb):
        print("Metodo non iterabile ciacia ")
        return [], 0, []
    else:
        # Lista di iterazioni
        xks = []
        eps = np.spacing(1)
        it = 0
        # Numero massimo di iterazioni
        nMax = int(math.ceil(3.3 * math.log10((b-a)/tol)))
        print(f"N passi necessari {nMax}")
        while it < nMax and abs(b-a) >= tol + eps * max(abs(a), abs(b)):
            # Calcolo il k esimo X
            xk = a + ((b-a)/2)
            xks.append(xk)
            it += 1
            if(sign(fname(xk)) == sign(fname(a))):
                a = xk
            elif(sign(fname(xk)) == sign(fname(b))):
                b = xk
            # Ho trovato lo Zero
            elif(fname(xk) == 0):
                break;
        return xk, it, xks
    
