# -*- coding: utf-8 -*-
"""
Es 2
"""

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import allM as fz

scelta = input("Scegli l'integrale da calcolare ")
x = sym.Symbol("x")
integrali = {
    "1" : [sym.log(x), 1, 2],
    "2" : [sym.sqrt(x), 0, 1],
    "3" : [sym.Abs(x), -1, 1]
    }
funzione, a, b = integrali.get(scelta)
f = sym.utilities.lambdify(x,funzione,np)
Iesatto = float(sym.integrate(funzione, (x, a, b)))
tol = 1.e-6
Is, Ns = fz.simpTol(f, a, b, tol)
It, Nt = fz.trapTol(f, a, b, tol)

print("Integrale esatto: ", Iesatto)
if Ns > 0:
    print("Simpson, integrale approssimato = ", Is, ", num segmenti = ", Ns)
if Nt > 0:    
    print("Trapezi, integrale approssimato = ", It, ", num segmenti = ", Nt)