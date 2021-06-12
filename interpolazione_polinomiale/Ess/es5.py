# -*- coding: utf-8 -*-
"""
ese5
"""


import numpy as np
import math 
from funzioni_Interpolazione_Polinomiale import InterpL
import matplotlib.pyplot as plt
#nodi del problema di interpolazione 
x=np.arange(0,2*math.pi+0.1,math.pi/2);
y1=np.sin(x)
xx=np.arange(0,2*math.pi+0.1,math.pi/40);