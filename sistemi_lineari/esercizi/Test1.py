# -*- coding: utf-8 -*-
"""
TEST 1
"""
import numpy as np
import numpy.linalg as npl
import math
import fz as fz
import matplotlib.pyplot as plt
import funzioni_Sistemi_lineari as fzz

errRelPivot = []
errRelNoPivot = []
n = range(5, 100, 1)
for el in n:
    A = np.empty((el,el), dtype=float)
    for i in range(el):
        for j in range(el):
            A[i,j] = math.sqrt(2/(el+1)) * math.sin((i + 1) * (j + 1) * math.pi/(el + 1))
    xesatta=np.arange(1,el+1).reshape((el,1))
    b=np.dot(A,xesatta)
    P,L,U = fz.LUsolveNoPivotVett(A)
    x = fz.LUsolve(L,U,P,b)
    
    P,L,U, = fz.solveLUPivot(A)
    xpiv= fz.LUsolve(P,L,U,b)
    
    errRelNoPivot.append(npl.norm(x-xesatta,1)/npl.norm(xesatta,1))
    errRelPivot.append(npl.norm(xesatta - xpiv, 1) / npl.norm(xesatta, 1))
   
    
    """       
    xEsatta = np.arange(1,el+1).reshape((el, 1))
    P, L, U, flag = fzz.LU_pivot(A)
    b = np.dot(A, xEsatta)
    xparziale = fzz.LUsolve(L, U, P, b)
    P, L, U, flag = fzz.LU_nopivotv(A)
    P = np.identity(el)
    xnopivot = fzz.LUsolve(L,U,P,b)
    # Uso la Norma al posto del |x|
    errRelPivot.append(npl.norm(xEsatta - xparziale, 1) / npl.norm(xEsatta, 1))
    errRelNoPivot.append(npl.norm(xEsatta - xnopivot, 1) / npl.norm(xEsatta, 1))
    """
plt.semilogy(n, errRelNoPivot, "r")
plt.semilogy(n, errRelPivot, "b")
plt.legend(["NoPivot", "Pivot"])
plt.show()