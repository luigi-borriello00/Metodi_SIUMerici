# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:25:29 2021

@author: damia
"""

import numpy as np
from funzioni_Interpolazione_Polinomiale import plagr
import matplotlib.pyplot as plt
scelta= input('Scegli nodi')


scelta_nodi={
    '1': np.arange(0,1.1,1/4),
    '2': np.array([-1, -0.7, 0.5, 1]) 
    } 

xnodi=scelta_nodi.get(scelta) 
n=xnodi.size

xx=np.linspace(xnodi[0],xnodi[n-1],200);

for k in range(n):
    p=plagr(xnodi,k)
    L=np.polyval(p,xx)
    plt.plot(xnodi,np.zeros((n,)),'ro');
    plt.plot(xnodi[k],1,'c*');
    plt.plot(xx,L,'b-');
    plt.show()


