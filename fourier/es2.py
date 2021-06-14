# -*- coding: utf-8 -*-
"""
Esercizio 2
Freq. basse -> grana grossa
Freq. alte -> dettaglio
 
"""

from scipy.fft  import fft
import math
import numpy as np
import matplotlib.pyplot as plt

def gradino(x):
    if x<-1 or x>1:
        f=1
    else:
        f=0
    return f

A = -3
B = 3
l = 0
r = 2 * math.pi

n = int(input("Introduci il valore di n "))
step = (B - A) / (n + 1)
y = []
x = np.arange(A, B, step)
for i in range(n + 1):
    y.append(gradino(x[i]))
c = fft(y)
a0 = c[0] / (n + 1)
if n % 2 == 0:
    m = n // 2
else:
    m = (n - 1) // 2
a = np.zeros((m + 2, ))
b = np.zeros((m + 2, ))
a[1 : m + 1] = 2 * c[1 : m + 1].real / (n + 1)
b[1 : m + 1] = -2 * c[1 : m + 1].imag / (n + 1)
if n % 2 == 0:
    a[m + 1] = 0
    b[m + 1] = 0
else:
    a[m + 1] = c[m + 1].real / (n + 1)
    b[m + 1] = 0
pol = a0 * np.ones((100,))
z = np.linspace(A, B, 100 )
zm = (z-A) * (r - l) / (B - A) + l
for k in range(1, m + 1):
    pol += a[k] * np.cos(k * zm) + b[k] * np.sin(k * zm)
    plt.plot(z, pol, "r", x, y, "o")
    plt.show()

