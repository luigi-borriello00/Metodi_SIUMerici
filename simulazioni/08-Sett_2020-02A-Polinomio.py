# -*- coding: utf-8 -*-
"""
Esame 8 Settembre
Es 2
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def Lagrange(xnodi, i):
    n = xnodi.size
    if i == 0:
        xzeri = xnodi[1 : n]
    else:
        xzeri = np.append(xnodi[0 : i], xnodi[i + 1 : n])
    num = np.poly(xzeri)
    den = np.polyval(num, xnodi[i])
    return num / den

def interpol(x, y, xx):
    m = x.size
    n = xx.size
    L = np.zeros((m,n))
    for i in range(m):
        L[i, :] = np.polyval(Lagrange(x,i), xx)
    return np.dot(y, L)

def chebishev(a, b, n):
    t1 = (a+b) / 2
    t2 = (b - a) / 2
    x = np.zeros((n + 1, ))
    for k in range(n+1):
        x[k] = t1 + t2 * np.cos(((2*k+1) / (2*(n + 1))*math.pi))
    return x

f = lambda x : 1 / (1 + 900 * (np.power(x, 2)))
xx = np.linspace(-1, 1, 100)
xe = []
xc = []
re = []
rc = []
LLe = np.zeros((6, 1))
LLc = np.zeros((6, 1))
l = 0
for n in range(5, 31, 5):
    xe = []
    xc = []
    Le = np.zeros((100, 1))
    Lc = np.zeros((100, 1))
    for i in range(1, n + 2):
        xe.append( -1 + ((2*(i-1)) / n))
    for i in range(n + 1, 0, -1):
        xc.append(math.cos(((2*i - 1) * math.pi) / (2 * (n + 1))))
    for i in range(n + 1):
        lagrC = Lagrange(np.array(xc), i)
        lagrE = Lagrange(np.array(xe), i)
        Le = Le + np.abs(np.polyval(lagrE, xx))
        Lc = Lc + np.abs(np.polyval(lagrC, xx))
    LLe[l] = np.max(Le)
    LLc[l] = np.max(Lc)
    l += 1

    fe = f(xe)
    fc = f(xc)
    ye = interpol(np.array(xe), fe, xx)
    yc = interpol(np.array(xc), fc, xx)
    re.append(np.abs(ye - f(xx)))
    rc.append(np.abs(yc - f(xx)))
    
    
for i in range(re.__len__()):
    plt.subplot(2, 3, i + 1)
    plt.plot(xx, re[i])
    plt.legend(["eq = " + str((i+1)*5)])
plt.show()
for i in range(rc.__len__()):
    plt.subplot(2, 3, i + 1)
    plt.plot(xx, rc[i])
    plt.legend(["cheb = " + str((i+1)*5)])
plt.show()

plt.semilogy(np.arange(5, 31, 5), LLe, "r-*", np.arange(5, 31, 5), LLc, "b-o")
plt.title("Costante di Lebesgue")
plt.legend(["Nodi equispaziati", "Nodi di chebishev"])
plt.show()