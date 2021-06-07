# -*- coding: utf-8 -*-
"""
Esercizio 8

"""

import numpy as np
import numpy.linalg as npl
import scipy.linalg as sci
import funzioni_Sistemi_lineari as fz
import matplotlib.pyplot as plt

def HankelModificata(n):
    A = np.zeros((n,n), dtype = float)
    for i in range(n):
        for j in range(n):
            if i == j or j == n-1:
                A[i,j] = 1
            elif i > j:
                A[i,j] = -1
            else:
                A[i,j] = 0
    return A

errRelPiv = []
errRelHou = []
indCond = []
for i in range(48,59,2):
    An = HankelModificata(i)
    xn = np.ones((i,1))
    b = np.dot(An,xn)
    indCond.append(npl.cond(An, 2))
    P,L,U,flag = fz.LU_pivot(An)
    if flag != 0:
        print("Sistema lineare non risolvibile con Strategia pivotale")
    else:
        x, flag = fz.LUsolve(L,U,P,b)
        errRelPiv.append(npl.norm(xn-x, 2) / npl.norm(xn,2))
    Q, R = sci.qr(An)
    # Risolvo y = Qt*b
    y = np.dot(Q.T, b)
    x, flag = fz.Usolve(R, y)
    errRelHou.append(npl.norm(xn-x, 2) / npl.norm(xn,2))
plt.plot(indCond, errRelPiv, "r", indCond, errRelHou, "b")
plt.legend(["Pivot", "QR"])
plt.xlabel("Indice di Condizionamento")
plt.ylabel("Errore relativo")
plt.show()
plt.plot(np.arange(48,59,2), errRelPiv, "-ro", np.arange(48,59,2), errRelHou, "-bo")
plt.legend(["Pivot", "QR"])
plt.xlabel("Grado della matrice")
plt.ylabel("Errore relativo")
plt.show()