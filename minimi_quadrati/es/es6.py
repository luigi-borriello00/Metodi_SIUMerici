# -*- coding: utf-8 -*-
"""
ese6
"""


import numpy as np
from funzioni_Interpolazione_Polinomiale import InterpL
import matplotlib.pyplot as plt
#nodi del problema di interpolazione 

T=np.array([-55, -45, -35, -25, -15, -5, 5, 15, 25, 35, 45, 55, 65])
L=np.array([3.7, 3.7,3.52,3.27, 3.2, 3.15, 3.15, 3.25, 3.47, 3.52, 3.65, 3.67, 3.52])

# punti di valutazione per l'interpolante
xx=np.linspace(np.min(T),np.max(T),200);


