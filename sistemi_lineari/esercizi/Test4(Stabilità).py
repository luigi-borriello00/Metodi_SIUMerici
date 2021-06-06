# -*- coding: utf-8 -*-
"""

Essendo E un moltiplicatore, quando diventa molto piccolo tende a far schizzare l'errore relativo
commesso, per questo si utilizza la tecnica di Pivoting

"""
import numpy as np
import numpy.linalg as npl
import funzioni_Sistemi_lineari as fz
import matplotlib.pyplot as plt

errRelPivot = []
errRelNoPivot = []

xEsatta = np.array([[2],[2]])
for k in range(2,19,2):
    E = 10**-k
    A = np.array([[E,1],[1,1]])
    b = np.array([2+E, 4]).reshape((2,1))
    P,L,U,flag = fz.LU_nopivot(A)
    if flag == 1:
        print(f"Non risolvibile con k = {k}")
    else:
         x, flag = fz.LUsolve(L,U,P,b)
         errRelNoPivot.append(npl.norm(x-xEsatta) / npl.norm(xEsatta))  

for k in range(2,19,2):
    E = 10**-k
    A = np.array([[E,1],[1,1]], dtype = float)
    b = np.array([2+E, 4],dtype = float).reshape((2,1))
    P,L,U,flag = fz.LU_pivot(A)
    if flag == 1:
        print(f"Non risolvibile con k = {k}")
    else:
         x, flag = fz.LUsolve(L,U,P,b)
         errRelPivot.append(npl.norm(x-xEsatta) / npl.norm(xEsatta))

plt.semilogy(np.arange(2,19,2), errRelNoPivot, "b")
plt.semilogy(np.arange(2,19,2), errRelPivot, "g")
plt.legend(["ErrRelNoPivot", "ErrRelPivot"])
plt.show()
