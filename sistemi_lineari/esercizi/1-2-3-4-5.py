# -*- coding: utf-8 -*-
"""
Es1
A triangolare sup
"""
import numpy as np

def uSolve(A, b):
    m,n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return []
    if np.all(np.diag(A)) != True:
         print('el. diag. nullo - matrice triangolare inferiore')
         x=[]
         return []
    x = np.zeros((m, 1))
    x[m-1] = b[m-1] / A[m-1, m-1]
    for i in range(m-1, -1, -1):
        somma = 0
        for j in range(i):
            somma += np.dot(A[i,j], x[j])
        x[i] = (b[i] - somma) / A[i,i]
    return x
    
    
def lSolve(A, b):
    m,n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return []
    if np.all(np.diag(A)) != True:
         print('el. diag. nullo - matrice triangolare inferiore')
         x=[]
         return []
    x = np.zeros((m, 1))
    x[0] = b[0] / A[0,0]
    for i in range(1, m):
        somma = 0
        for j in range(i+1, m, 1):
            somma += np.dot(A[i,j], x[j])
        x[i] = (b[i] - somma) / A[i,i]
    return x

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
    y = lSolve(L, Pb)
    x = uSolve(U, y)
    return x

""" ESERCIZIO 4 """
def LUsolveNoPivot(A):
    m, n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return [],[]
    L = np.identity(m)
    U = A.copy()
    for k in range(n):
        if U[k,k] == 0:
            print("Pivot nullo")
            return [],[]
        for i in range(k+1, n, 1):
            m = U[i,k] / U[k,k]
            L[i,k] = -m
            for j in range(k+1, n, 1):
                U[i,j] = U[i,j] - m * U[k,j]
    return L,U
    
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