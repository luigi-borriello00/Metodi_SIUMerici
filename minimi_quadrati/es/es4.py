# -*- coding: utf-8 -*-
"""
ese4
"""

import numpy as np
from funzioni_Interpolazione_Polinomiale import plagr
import matplotlib.pyplot as plt

scelta= input('Scegli nodi ')
scelta_nodi={
    '1': np.arange(0,1.1,1/4),
    '2': np.array([-1, -0.7, 0.5, 1]) 
    } 

xnodi=scelta_nodi.get(scelta) 
nodiLagr = []
n=xnodi.size
xx = np.linspace(xnodi[0], xnodi[n-1], 100)
for i in range(n):
    L = np.polyval(plagr(xnodi, i), xx)
    plt.plot(xnodi,np.zeros((n,)),'ro');
    plt.plot(xnodi[i],1,'c*');
    plt.plot(xx,L,'b-');
    plt.show()

