# -*- coding: utf-8 -*-
"""
ese9
"""

import numpy as np
from funzioni_Interpolazione_Polinomiale import plagr
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
