# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:09:00 2021

@author: Luigi
"""
import numpy as np
import scipy as sci
from scipy.linalg import qr
import matplotlib.pyplot as plt

def Usolve(U, b):
    m, n = U.shape
    if m != n:
        print("Matr non quadrata")
        return [], 1
    x = np.zeros((m,))
    x[m-1] = b[m - 1] / U[m-1, n-1]
    for i in range(m - 2, -1, -1):
        x[i] = (b[i] - (np.dot(U[i, i+1 : m], x[i + 1 : m]))) / U[i,i]
        
    return x, 0

"""
    Qy = b
    Rx = y

"""
def metodoQR(x, y, n):
    H = np.vander(x, n+1)
    Q,R = qr(H)
    y1 = np.dot(Q.T, y)
    a, flag = Usolve(R[:n+1,:], y1[:n+1])
    return a

x = np.arange(1900, 2020, 10, dtype = float)
y = np.array([76,92,106,123,132,151,179,203,226,249,281,305], dtype = float)
print(x)

x1 = metodoQR(x, y, 1)
x2 = metodoQR(x, y, 2)
x3 = metodoQR(x, y, 3)

xx = np.linspace(np.min(x), np.max(x), 100)
pol1 = np.polyval(x1, xx)
pol2 = np.polyval(x2, xx)
pol3 = np.polyval(x3, xx)

plt.plot(x, y, "o", xx, pol1, xx, pol2, xx, pol3)
plt.legend(["Nodi", "Pol. 1", "Pol. 2", "Pol. 3"])
plt.show()

# Punto D
err1 = []
err2 = []
err3 = []
for i in range(12):
    err1.append((pol1[i] - y[i]) ** 2)
    err2.append((pol2[i] - y[i]) ** 2)
    err3.append((pol3[i] - y[i]) ** 2)
    
plt.plot(np.arange(12), err1, np.arange(12), err2, np.arange(12), err3)
plt.legend(["Err1", "Err2", "Err3"])
plt.show()

""" OSSERVIAMO CHE I POLINOMI DI GRADO 2 E 3 DANNO LUOGO AGLI STESSI ERRORI
"""
    
    
    
    