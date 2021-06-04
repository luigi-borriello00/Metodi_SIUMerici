# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:24:02 2021

@author: Luigi
"""
import numpy as np
import allMethods as fz
import sympy as sym
import sympy.utilities.lambdify
import matplotlib.pyplot as plt

c=[1/20, 1/6, 3/10, 2/5]

x = sym.symbols("x")
x0 = 2.5
tolx = 1.e-8

for ci in c:
    gx = x - (ci * x**2) + 5*ci
    g = sym.lambdify(x, gx, np)
    xk, it, xks = fz.iterazione(g, x0, tolx, 200)
    print("Usando c = {:f} ottengo un xk = {:e} con {:d} iterazioni".format(ci, xk, it))
    z = np.linspace(0,3,20)
    plt.plot(z,z, "g")
    plt.plot(z, g(z), "r")
    plt.plot(xks, np.zeros((it+1,1)), "-bo")
    plt.title(f"Con c = {ci}")
    print(xks)
    #Grafico della poligonale  
    Vx=[]
    Vy=[]
    for k in range(it):
        Vx.append(xks[k])
        Vy.append(xks[k])
        Vx.append(xks[k])
        Vy.append(xks[k+1])
    Vy[0] = 0
    plt.plot(Vx,Vy,'y',)

  
    plt.show()