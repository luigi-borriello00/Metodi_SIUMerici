# -*- coding: utf-8 -*-
"""
Segnale sporco
"""
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math

segnale = lambda x : np.sin(2 * math.pi * 4 * x) + np.sin(2 * math.pi * 15 * x)
rumore = lambda x : np.sin(2 * math.pi * 40 * x)

T = 1
Fs = 80
N = T * Fs

# Campiono il tempo
t = np.linspace(0, 80, 80)
plt.plot(t, segnale(t))
plt.title("Segnale esatto")
plt.show()

y = segnale(t) + rumore(t)
plt.plot(t, y)
plt.title("Segnale sporco")
plt.show()

# Plotto lo spettro
delta_u = Fs / N
freq = np.arange(- Fs / 2, Fs / 2, delta_u)
c = sci.fftpack.fftshift(sci.fft(y))
plt.plot(freq, np.abs(c))
plt.title("Spettro segnale rumoroso")
plt.show()

# Pulisco Freq > 15
ind = np.abs(freq) > 15
c[ind] = 0
sign = sci.ifft(sci.fftpack.ifftshift(c))
plt.plot(freq, np.abs(c))
plt.title("Spettro segnale ripulito")
plt.show()

plt.plot(t, sign, "b", t, segnale(t), "r")
plt.title("Segnale ripulito")
plt.legend(["Segnale ricostruito", "Segnale originale"])
plt.show()
