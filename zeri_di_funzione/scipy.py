# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:59:22 2021

@author: kelvi
"""

import sympy as sym
from sympy.utilities.lambdify import lambdify
import numpy as np

x = sym.symbols('x')

fx= sym.exp(-x) - (x + 1)
print(fx)
dfx = sym.diff(fx, x, 1)
print(dfx)

#Trasformo in funzione numerica la funzione simbolica
f = lambdify(x, fx, np) # np serve per indicare che la lamba puo lavorare anche con gli array di np
df = lambdify(x, fx, np) # quindi np la rende una ufunc

