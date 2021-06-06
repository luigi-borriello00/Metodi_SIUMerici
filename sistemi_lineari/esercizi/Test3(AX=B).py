# -*- coding: utf-8 -*-
"""
Test 3

AX=B
risolvo n sistemi lineari 
Axi = bi dove
    Ly = Pb e Ux = y

Se usiamo B come la matrice identità in X troveremo l'inversa
"""
import numpy as np
import funzioni_Sistemi_lineari as fz
import scipy.linalg as sci

scelta = input("Seleziona Matrice ")
matrici = {
    "1" : np.array([[3,5,7],[2,3,4],[5,9,11]], dtype = float),
    "2" : np.array([[1,2,3,4],[2,-4,6,8],[-1,-2,-3,-1],[5,7,0,1]], dtype = float)
    }
A = matrici.get(scelta)
m, n = A.shape
B = np.identity(m)
X = fz.solve_nsis(A,B)
print(f"L'inversa di A calcolata con n Sistemi Lineari è \n {X}")
print(f"L'inversa calcolata con Scipy è \n {sci.inv(A)}")
