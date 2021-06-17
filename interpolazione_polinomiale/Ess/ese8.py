# -*- coding: utf-8 -*-
"""
ese9
"""

import numpy as np
import interpolL as fz
import math

def zeri_Cheb(a,b,n):
    t1=(a+b)/2
    t2=(b-a)/2
    x=np.zeros((n+1,))
    for k in range(n+1):
        x[k]=t1+t2*np.cos(((2*k+1)/(2*(n+1))*math.pi))

    return x

#calcolo della costante di lebesgue in [-1,1]

xx=np.linspace(-1,1,200);
LLe = np.zeros((4,1))
LLc = np.zeros((4,1))
l = 0
for n in range(5,25,5):
    xC = zeri_Cheb(-1, 1, n)
    xE = np.linspace(-1, 1, n+1)
    Le = np.zeros((200,1))
    Lc = np.zeros((200,1))
    for i in range(n+1):
        lagrC = fz.polinomioLagrange(xC, i)
        lagrE = fz.polinomioLagrange(xE, i)
        Le = Le + np.abs(np.polyval(lagrE, xx))
        Lc = Lc + np.abs(np.polyval(lagrC, xx))

    LLe[l] = np.max(Le)
    LLc[l] = np.max(Lc)
    l += 1
        
print("Costante di Lebesgue con nodi equispaziati ", LLe)
print("Costante di Lebesgue con nodi di Cheb ", LLc)
