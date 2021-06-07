# -*- coding: utf-8 -*-
"""
Es1
A triangolare sup
"""
import numpy as np

def Usolve(U, b):
    m,n = U.shape
    x = np.zeros((m,1))
    if m != n or np.all(np.diag(U)) != True:
        print("Matrice non risolvibile")
        return [], 1
    for k in reversed(range(n)):
        x[k] = (b[k] - np.dot(U[k, k+1:n], x[k+1:n])) / U[k,k]
    return x, 0

def Lsolve(L,b):
    m,n = L.shape
    if m != n or np.all(np.diag(L)) != True:
        print("Matrice non risolvibile")
        return [], 1
    x = np.zeros((n, 1))
    for k in range(n):
        x[k] = (b[k] - np.dot(L[k, 0:k], x[0:k])) / L[k,k]
    return x, 0



"""
    ESERCIZIO 3
    Parto da PAx = b
    ottengo Ax = Pb
    nonchè LUx = Pb
    pongo Ux = y
    Ottenendo 
    { Ux = y
     Ly = Pb
    }               """
def LUsolve(P, L, U, b):
    # Risultati Permutati
    Pb = np.dot(P,b)
    y = Lsolve(L, Pb)
    x = Usolve(U, y)
    return x

""" ESERCIZIO 4 """

def LUnoPivot(A):
    m,n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return [],[],[], 1
    if np.all(np.diag(A)) != True:
        print("Elemento diagonale nullo")
        return [], [], [], 1
    U = A.copy()
    for k in range(n-1):
        if U[k,k] == 0:
            print("Elemento diagonale nullo")
            return [], [], [], 1
        for i in range(k+1, n-1):
            U[k,i] = U[k,i] / U[k,k]
            for j in range(k+1, n-1):
                U[i,j] = U[i,j] - np.dot(U[i,k], U[k,j])
    L = np.ltril(U,-1) + np.identity(m)
    U = np.utril(U)
    P = np.identity(m)
    return P,L,U,0


def LUsolveNoPivotVett(A):
    m, n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return [],[]
    U = A.copy()
    k = n
    if U[:k, :k] == 0:
            print("Pivot nullo")
            return [],[]
    i = n
    j = n
    for k in range(n-1):
        U[k+1 : i, k] = U[k + 1 : i, k] / U[k, k]
        U[k+1 : i, k+1 : j] = U[k+1 : i, k+1 : j] - U[k+1 : i, k] * U[k, k+1 : j]
        
    L = np.tril(U,-1) + np.identity(m)
    U = np.triu(U)
    return L,U



""" ESERCIZIO 5"""
def solveLUPivot(A):
    m,n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return [], [], []
    U = A.copy()
    P = np.identity(m)
    for k in range(n-1):
        pivot = np.argmax(abs(U[:,k]))
        if pivot != k:
            U[[k, pivot], :] = U[[pivot, k], :]
            P[[k, pivot], :] = P[[pivot, k], :]
        U[k+1 : n, k] = U[k + 1 : n, k] / U[k, k]
        U[k+1 : n, k+1 : n] = U[k+1 : n, k+1 : n] - U[k+1 : n, k] * U[k, k+1 : n]
    L = np.tril(U, k=-1) + np.identity(m)
    U = np.triu(U)
    return L, U, P