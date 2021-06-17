# -*- coding: utf-8 -*-
"""
ES 1

"""
import numpy as np

"""

Punto A: la matrice A non ammette la fattorizzazione LU senza pivoting non avendo tutti i determinanti
            delle sottomatrici di testa != 0
            Metre la matrice B rispetta questa condizione dunque ammette tale fattorizzazione
            
"""

"""
Punto B
"""

def LUnoPivot(M):
    m, n = M.shape
    if m != n:
        print("Matrice non quadrata")
        return [], [], [], 1
    U = M.copy()
    for i in range(n):
        if U[i, i] == 0:
            print("Elemento diagonale nullo ")
            return [], [], [], 1
    for k in range(n - 1):
        U[k + 1 : n, k] = U[k + 1 : n, k] / U[k,k]
        U[k + 1 : n, k + 1] = U[k + 1 : n, k + 1] - (U[k + 1 : n, k] * U[k, k + 1 : n])
    L = np.tril(U, -1) + np.eye(n)
    U = np.triu(U)
    return L, U, np.eye(n), 0


B = np.array([[5, -2, 2, 0],
              [-2, 5, 0, 1],
              [2, 0, 5, 1],
              [0, 1, 1, 5]])
L, U, P, flag = LUnoPivot(B)
p1 = P.copy()
m, n = U.shape
p1[[0, n-1]] = p1[[n-1, 0]]
p1[[1, 2]] = p1[[2, 1]]
print(p1)
det = 1
det2 = 1
U2 = U * p1
for k in range(n):
    det *= U[k,k]
