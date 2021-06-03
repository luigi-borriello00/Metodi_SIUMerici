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

def sign(x) : math.copysign(1, x)

def bisezione(fname, a, b, tol):
    if sign(fname(a)) == sign(fname(b)):
        print("Metodo non iterabile ciacia")
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
            xks.append(a + ((b-a)/2))
            if(math.copysign(1, xks[it]) == math.copysign(1, a)):
                a = xks[it]
            elif(math.copysign(1, xks[it]) == math.copysign(1, b)):
                b = xks[it]
            # Ho trovato lo Zero
            elif(fname(xks[it]) == 0):
                break;
            it += 1
        
        return xks[it], it+1, xks
    
