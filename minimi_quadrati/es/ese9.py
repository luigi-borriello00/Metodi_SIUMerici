# -*- coding: utf-8 -*-
"""
ese9
"""
import numpy as np
import numpy.linalg as npl
from funzioni_Interpolazione_Polinomiale import InterpL
import math
import matplotlib.pyplot as plt

f= lambda x: np.sin(2*math.pi*x)
x=np.linspace(-1,1,22)
y1=f(x);

y2=y1.copy()
y2=y2+0.0002*np.random.randn(22,)

