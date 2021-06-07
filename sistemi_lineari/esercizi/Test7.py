# -*- coding: utf-8 -*-
"""
Es 7

QR piu stabile
R è maggiorata dalla radice di n + max di aij
"""
import numpy as np
import numpy.linalg as npl
import scipy.linalg as sci
import funzioni_Sistemi_lineari as fz
import matplotlib.pyplot as plt

def Hankel(n):
    A = np.zeros((n,n), dtype = float)
    for i in range(n):
        for k in range(i+1-n, i+1):
            if k > 0:
                A[i,n-1+k-i] = 2.0**(k+1)
            else:
                A[i,n-1+k-i] = 2.0**(1/(2-k-1))
    return A

errRelPiv = []
errRelHou = []
indCond = []
for i in range(4,41,6):
    An = Hankel(i)
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