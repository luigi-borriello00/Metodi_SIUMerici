# -*- coding: utf-8 -*-
"""
Filtraggio di un segnale nel dominio di FOurier
Come operare:
    Dato un segnale rumoroso, ne calcolo le trasformate di Fourier
    Pulisco i coefficenti e ricostruisco nella maniera inversa la funzione
    
"""

from scipy.fft  import fft, ifft
from scipy.fftpack import fftshift, ifftshift
import math
import numpy as np
import matplotlib.pyplot as plt

# Segnale, e segnale rumoroso
f = lambda x : np.sin(2 * math.pi * 5 * x) + np.sin(2 * math.pi * 10 * x)
noise = lambda x : 2 * np.sin(2 * math.pi * 30 * x)

T = 2     # Durata del segnale
Fs = 100  # Frequenza di campionamento nel dominio del tempo: Numero di campioni al secondo (maggiore uguale del doppio della freqeunza massima nel dominio delle frequenze
        # (wmax) presente nel segnale)
dt = 1 / Fs # Passo di campionamento nel dominio del tempo
N = T * Fs  # Numero di campioni: durata in secondi per numero di campioni al secondo

# Campionamento del dominio temporale
t = np.linspace(0, T, N)

# Campionamento del segnale rumoroso
y = f(t) + noise(t)
plt.plot(t, y, 'r-')
plt.title('Segnale rumoroso')
plt.xlabel("Tempo")
plt.show()
plt.plot(t,f(t),'b-')
plt.title('Segnale esatto')
plt.xlabel("Tempo")
plt.show()

# Passo di campionamento nel dominio di Fourier (si ottiene dividendo per N l'ampiezza del range che contiene le frequenze)
delta_u = Fs / N
# Fs è il doppio della freq. max presente nel segnale
# Dunque la freq varia tra -Fs / 2 a +Fs / 2
freq = np.arange(-Fs / 2, Fs / 2, delta_u)  # Il range delle frequenza varia tra -fs/2 ed fs/2
# Riordina le freq nel vettore mettendo al centro le freq piu basse
c = fftshift(fft(y))

plt.plot(freq, np.abs(c))
plt.xlabel("Frequenza")
plt.ylabel("Coeff. di Fourier(Spettro)")
plt.title('Spettro Fourier segnale rumoroso')
plt.show()
ind = np.abs(freq) > 10.0

# Annulliamo i coefficienti di Fourier esterni all'intervallo di frequenze [-10,10]
c[ind] = 0
plt.plot(freq,np.abs(c))
plt.title('Spettro Fourier segnale Filtrato')
plt.show()
#Ricostruiamo il segnale a partire dai coefficienti du Fourier filtrati
rec = ifft(ifftshift(c))
plt.plot(t, rec, t, f(t))
plt.legend(['Segnale filtrato', 'Segnale originale'])



