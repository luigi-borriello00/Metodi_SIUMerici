# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:56:17 2021

@author: Luigi
"""
import numpy as np
import scipy as sci
import sympy as sym
import matplotlib.pyplot as plt

def Lagrange(xnodi, i):
    if i == 0:
        xzeri = xnodi[1:]
    else:
        xzeri = np.append(xnodi[:i], xnodi[i + 1 :])
    num = np.poly(xzeri)
    den = np.polyval(num, xnodi[i])
    return num / den
        
def Interpol(x, y, xx):
    m = x.size
    n = xx.size
    L = np.zeros((m,n))
    for k in range(m):
        L[k, :] = np.polyval(Lagrange(x, k), xx)
    return np.dot(y, L)

def simpsonComp(f, a, b, n):
    h = (b - a) / (2 * n)
    interv = np.arange(a, b + h, h)
    fnodi = f(interv)
    I = h * (fnodi[0] + 2 * np.sum(fnodi[2 : 2*n : 2]) + 4 * np.sum(fnodi[1 : 2*n : 2]) + fnodi[2*n]) /3
    return I

def simpsonTol(f, a, b, tol):
    N = 1
    nMax = 2048
    err = 1
    In = simpsonComp(f, a, b, N)
    while err >= tol and N < nMax:
        N *= 2
        I2n = simpsonComp(f, a, b, N)
        err = np.abs(I2n - In) / 15
        In = I2n
    return In, N

f = lambda x : x - np.sqrt(x - 1)
a = 1
b = 3
x = np.linspace(a, b, 4)
xx = np.linspace(a, b, 100)
y = f(x)
yy = Interpol(x, y, xx)

plt.plot(xx, yy, xx, f(xx), x, y, "o")
plt.legend(["Polinomio di grado 3", "Funzione", "Nodi di interpolazione"])
plt.show()

n = 4
p = lambda nodi : Interpol(x, y, nodi)
I1, N1 = simpsonTol(f, a, b, 10**-5)
print(f"Sono necessare {N1} iterazioni per I1")
I2, N2 = simpsonTol(p, a, b, 10**-5)
print(f"Sono necessare {N2} iterazioni per I2")
I1es = 2.114381916835873
I2es = 2.168048769926493
err1 = abs(I1es - I1)
err2 = abs(I2es - I2)
print("ErrRel I1 = ", err1)
print("ErrRel I2 = ", err2)
