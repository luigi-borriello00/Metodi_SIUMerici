# -*- coding: utf-8 -*-
"""
es7
"""


import numpy as np
import interpolL as fz
import matplotlib.pyplot as plt
import math
from funzioni_Interpolazione_Polinomiale import InterpL


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

n=int(input('Grado del polinomio '))
scelta_punti = {
        '1': np.linspace(a,b,n+1),
        '2': zeri_Cheb(a,b,n)
        }
x=scelta_punti.get(sceltap)
xx = np.linspace(a,b,200)
y = f(x)
yy = f(xx)
p = fz.interpolL(x, y, xx)

err = (np.abs(f(xx) - p) )
plt.plot(x, y, "ro", xx, p, "g", xx, f(xx), "b")
plt.legend(["Pti interpolazione", "Polinomio", "Funzione"])
plt.show()
plt.plot(xx, err)
plt.title("ErroreRel")
plt.show()