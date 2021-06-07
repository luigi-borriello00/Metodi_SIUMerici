# -*- coding: utf-8 -*-
"""
es7
"""


import numpy as np
from funzioni_Interpolazione_Polinomiale import InterpL
import matplotlib.pyplot as plt
import math


def zeri_Cheb(a,b,n):
    t1=(a+b)/2
    t2=(b-a)/2
    x=np.zeros((n+1,))
    for k in range(n+1):
        x[k]=t1+t2*np.cos(((2*k+1)/(2*(n+1))*math.pi))

    return x
                          
                          
                          
                          
sceltaf=input("Scegli funzione ")
 
scelta_funzione = {
        '1': [lambda x: np.sin(x)-2*np.sin(2*x),-math.pi, math.pi],
        '2': [lambda x: np.sinh(x),-2,2],
        '3': [lambda x: np.abs(x), -1,1],
        '4': [lambda x: 1/(1+x**2), -5,5]
}

f,a,b=scelta_funzione.get(sceltaf)

sceltap= input("Scegli tipo punti : 1(equidistanti) 2(Chebishev)\n ")

n=int(input('Grado del polinomio'))

scelta_punti = {
        '1': np.linspace(a,b,n+1),
        '2': zeri_Cheb(a,b,n)
        }

x=scelta_punti.get(sceltap)





