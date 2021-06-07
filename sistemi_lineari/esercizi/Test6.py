# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:46:43 2021

@author: Luigi
"""

import funzioni_Sistemi_lineari as fz
import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt

n = 100
v = np.random.rand(n, 1)
# V deve avere norma 2 unitaria quindi pari a 1, di conseguenza tutti gli elementi devono essere
# < di 0
v=v/npl.norm(v,2);

Q = np.eye(n)-2*np.outer(v,v.T)
xesatta = np.ones((n,1))
errRelNoPiv = []
errRelPiv = []
indCond = []
D = np.identity(n)
for k in range(1,21):
    D[n-1,n-1] = 10**k
    A = np.dot(Q,D)
    indCond.append(npl.cond(A, 2))
    b = np.dot(A,xesatta)
    # No Pivot
    P,L,U,flag = fz.LU_nopivot(A)
    if flag != 0:
        print("NON RISOLVIBILE SENZA PIVOTING")
    else:
        x, flag = fz.LUsolve(L,U,P,b)
        errRelNoPiv.append(npl.norm(x-xesatta,1)/npl.norm(xesatta,1))
    # Pivot
    P,L,U,flag = fz.LU_pivot(A)
    if flag != 0:
        print("NON RISOLVIBILE CON PIVOTING")
    else:
        x, flag = fz.LUsolve(L,U,P,b)
        errRelPiv.append(npl.norm(x-xesatta,1)/npl.norm(xesatta,1))
plt.loglog(indCond, errRelNoPiv, "-or", indCond, errRelPiv, "-ob")
plt.legend(["SenzaPivot", "ConPivot"])
plt.show()