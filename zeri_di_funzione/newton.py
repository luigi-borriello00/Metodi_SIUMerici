# -*- coding: utf-8 -*-
"""
NEWTON

Controllo per ogni i sulla derivata > spacing

Controllo su:
    - nIter
    - Residuo
    - ErrRel
"""

import numpy as np

def newton(fname, fpname, x0, tolx, tolf, nMaxIt):
    xk = []
    it = 0
    if fpname(x0) <= np.spacing(1):
        print("Derivata nulla in x0")
        return [], 0, []
    else:
        d = (fname(x0)/ fpname(x0))
        x1 = x0 - d
        xk.append(x1)
        it += 1
        while it < nMaxIt and fname(x1) >= tolf and abs(d) >= tolx * abs(x1):
            x0 = x1
            if fpname(x0) <= np.spacing(1):
                print("Derivata nulla in x0")
                return xk[it], it, xk
            d = x0 - (fname(x0)/ fpname(x0))
            x1 = x0 - d
            xk.append(x1)
            it += 1
            if it == nMaxIt:
                print("Numero massimo di iterazioni raggiunto")
        return xk[it-1], it, xk