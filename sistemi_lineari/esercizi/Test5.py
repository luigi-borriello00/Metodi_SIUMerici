# -*- coding: utf-8 -*-
"""
Test 5
testiamo come utilizzando il pivoting i |moltiplicatori| sono tutti < 1
"""

import funzioni_Sistemi_lineari as fz
import numpy as np

scelta = input("Seleziona Matrice ")
matrici = {
    "1" : [np.array([[3,1,1,1], [2,1,0,0], [2,0,1,0], [2,0,0,1]],dtype=float),
            np.array([[4],[1],[2],[4]],dtype=float),
            np.array([1,-1,0,2],dtype=float).reshape((4,1))],
    "2" : [np.array([[1,0,0,2], [0,1,0,2], [0,0,1,2], [1,1,1,3]],dtype=float),
            np.array([[4],[1],[2],[4]],dtype=float),
            np.array([2,-1,0,1],dtype=float).reshape((4,1))], 
    }
A, b, xEsatto = matrici.get(scelta)

P,L,U,flag = fz.LU_nopivot(A)
if flag != 0:
    print("Non risolvibile senza pivoting")
else:
    uMax = np.max(np.abs(U))
    lMax = np.max(np.abs(L))
    x, flag = fz.LUsolve(L,U,P, b)
    print(f"Usando no-pivot \n {x}")
    print("Elemento max di U = ",uMax,", elemento max di L = ",lMax)
    
P,L,U,flag = fz.LU_pivot(A)
if flag != 0:
    print("Non risolvibile con pivoting")
else:
    uMax = np.max(np.abs(U))
    lMax = np.max(np.abs(L))
    x, flag = fz.LUsolve(L,U,P, b)
    print(f"Usando pivot \n {x}")
    print("Elemento max di U = ",uMax,", elemento max di L = ",lMax)