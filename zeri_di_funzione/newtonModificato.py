# -*- coding: utf-8 -*-
"""
Metodo di Newton

Differenza: Ogni incremento va moltiplicato per m
"""
import numpy as np

def newtonModificato(fname, fpname, x0, tolx, tolf, nMaxIt, m):
    xk = []
    it = 0
    if abs(fpname(x0)) <= np.spacing(1):
        print("Derivata nulla in x0")
        return [], 0, []
    else:
        d = (fname(x0)/ fpname(x0))
        x1 = x0 - d*m
        xk.append(x1)
        it += 1
        while it < nMaxIt and abs(fname(x1)) >= tolf and abs(d) >= tolx * abs(x1):
            x0 = x1
            if abs(fpname(x0)) <= np.spacing(1):
                print("Derivata nulla in x0")
                return x1, it, xk
            d = (fname(x0)/ fpname(x0))
            x1 = x0 - d*m
            xk.append(x1)
            it += 1
            
        if it == nMaxIt:
            print("Numero massimo di iterazioni raggiunto")
        return x1, it, xk