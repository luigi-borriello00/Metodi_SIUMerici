# -*- coding: utf-8 -*-
"""
Es 2
Il metodo senza pivot non funziona poiche abbiamo un elemento sulla diagonale di A1 nullo
"""
import funzioni_Sistemi_lineari as fz
import numpy as np

A1 = np.array([1,2,3,0,0,1,1,3,5], dtype=float).reshape((3,3))
b1 = np.array([6,1,9], dtype=float)
A2 = np.array([1,1,0,3,2,1,-1,1,-1,2,3,-1,3,-1,-1,2], dtype=float).reshape((4,4))
b2 = np.array([5,3,3,3], dtype=float)

xEsatta = np.ones((A1.shape[0], 1))


P, L, U, flag = fz.LU_nopivot(A1)
if flag == 0:
    xNoPiv, flag = fz.LUsolve(L,U,P, b1)
    print(f"A1 no pivot{xNoPiv}")
else:
    print("A1 Non risolvibile senza Pivot")    

P, L, U, flag = fz.LU_nopivot(A2)
if flag == 0:
    xNoPiv, flag = fz.LUsolve(L,U, P, b2)
    print(f"A2 no pivot{xNoPiv}")
else:
    print("A2 Non risolvibile senza Pivot")    

# CON PIVOTING

P, L, U, flag = fz.LU_pivot(A1)
if flag == 0:
    xPiv, flag = fz.LUsolve(L,U,P, b1)
    print(f"A1 con pivot{xPiv}")
else:
    print("A1 Non risolvibile con Pivot")    

P, L, U, flag = fz.LU_pivot(A2)
if flag == 0:
    xPiv, flag = fz.LUsolve(L,U, P, b2)
    print(f"A2 con pivot{xPiv}")
else:
    print("A2 Non risolvibile con Pivot") 