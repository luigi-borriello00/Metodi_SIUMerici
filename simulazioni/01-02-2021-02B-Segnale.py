# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:16:02 2021

@author: Luigi
"""

import numpy as np
import scipy as sci
from scipy.fftpack import fftshift, ifftshift
import matplotlib.pyplot as plt
import math

s1 = lambda x : 4 * np.sin(15 * x)
s2 = lambda x : 3 * np.sin(40 * x)
s3 = lambda x : 2 * np.sin(60 * x)

segnale = lambda x : s1(x) + s2(x) + s3(x)

rumore = lambda x : 2 * np.sin(80 * x)

T = 2
Fs = 170
N = Fs * T

t = np.linspace(0, 2, N)
plt.plot(t, segnale(t))
plt.title("Segnale Originale")
plt.show()

y = segnale(t) + rumore(t)
plt.plot(t, y)
plt.title("Segnale Sporco")
plt.show()

deltaU = Fs / N
freq = np.arange(-Fs/2, Fs/2, deltaU)

c = fftshift(sci.fft(y))
plt.plot(freq, np.abs(c))
plt.title("Spettro Segnale Rumoroso")
plt.show()

ind = np.abs(freq) > 10
c[ind] = 0
plt.plot(freq, np.abs(c))
plt.title("Spettro Segnale Ripulito")
plt.show()

segn = sci.ifft(ifftshift(c))
plt.plot(t, segn, t, segnale(t))
plt.title("Segnale Ricostruito")
plt.show()