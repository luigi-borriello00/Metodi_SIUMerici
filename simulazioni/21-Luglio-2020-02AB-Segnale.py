# -*- coding: utf-8 -*-
"""
Es2 part 2
"""

import numpy as np
import scipy as sci
from scipy.fftpack import fftshift, ifftshift
import matplotlib.pyplot as plt
import math


f1 = lambda x : 4 * np.sin(25 * x)
f2 = lambda x : 3 * np.sin(60 * x)
disturbo = lambda x : 2 * np.sin(110 * x)

T = 4
Fs = 230
N = 4 * 230

t = np.linspace(0, T, 920)
ft = f1(t) + f2(t)
plt.plot(t, ft)
plt.title("Segnale pulito")
plt.show()

y = ft + disturbo(t)
plt.plot(t, y)
plt.title("Segnale sporco")
plt.show()

c = fftshift(sci.fft(y))
deltaU = (Fs / N)
freq = np.arange(-Fs/2, Fs/2, deltaU)
plt.plot(freq, np.abs(c))
plt.title("Spettro segnale rumoroso")
plt.show()
ind = np.abs(freq) > 15
c[ind] = 0
plt.plot(freq, np.abs(c))
plt.title("Spettro segnale ripulito")
plt.show()
pulito = sci.ifft(ifftshift(c))
plt.plot(t, ft, t, pulito)
plt.legend(["Originale", "Ricostruito"])
plt.title("Segnale ricostruito")
plt.show()

