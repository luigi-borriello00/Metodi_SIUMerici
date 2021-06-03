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
        while it < nMax and abs(b-a) >= tol + eps * max(abs(a), abs(b)):
            # Calcolo il k esimo X
            xk = a + ((b-a)/2)
            xks.append(xk)
            if(sign(xks[it]) == sign(a)):
                a = xks[it]
            elif(sign(xks[it]) == sign(b)):
                b = xks[it]
            # Ho trovato lo Zero
            elif(fname(xks[it]) == 0):
                break;
            it += 1
        
        return xk, it+1, xks
    
