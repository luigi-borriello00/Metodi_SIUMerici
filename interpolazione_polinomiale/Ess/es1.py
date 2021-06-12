# -*- coding: utf-8 -*-
"""
Ese1

@author: damia
"""
import numpy as np
import matplotlib.pyplot as plt
from funzioni_Approssimazione_MQ import metodoQR
scegli_set=input('Scegli set dati')



scelta_dati = {
        '1': [np.array([-3.5,-3, -2, -1.5, -0.5, 0.5, 1.7, 2.5, 3]),np.array([-3.9,-4.8,-3.3,-2.5, 0.3,1.8,4,6.9,7.1])],
        '2': [np.array([-3.14,-2.4,-1.57,-0.7,-0.3,0.0,0.4,0.7,1.57]),np.array([0.02,-1,-0.9,-0.72, -0.2,-0.04,0.65, 0.67,1.1])],
        '3': [np.linspace(0,3,12),np.exp(np.linspace(0,3,12))*np.cos(np.linspace(0,3,12))+np.random.randn((12,))],
        '4': [np.array([1.001,1.0012,1.0013,1.0014, 1.0015, 1.0016]),np.array([-1.2,-0.95,-0.9, -1.15,-1.1, -1])]
}
x,y=scelta_dati.get(scegli_set) 


