# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:05:31 2021

@author: Luigi
"""

import numpy as np
import sympy as sym
import sympy.utilities.lambdify
import allMethods as fz

x = sym.symbols("x")
fx = sym.atan(x)
dfx = sym.diff(fx, x, 1)

f = sym.lambdify(x, fx, np)
df = sym.lambdify(x, dfx, np)

x0 = [1.2, 1.4]
tolx = 1e-6
tolf = 1e-5

for el in x0:
    xk, it, xks = fz.newton(f, df, el, tolx, tolf, 500)
    print("Con xo = {:f} abbiamo xk = {:e} con {:d} iterazioni".format(el,xk,it))
