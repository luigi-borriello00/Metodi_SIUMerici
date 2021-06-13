# -*- coding: utf-8 -*-
"""
Mappiamo un intervallo [A, B) in [l, r)
                        x -> xm

xm = ((x-A) / B-A) * (r-l) + l

[l, r) corrisponde a [0, 2PIG)

"""

from scipy.fft  import fft
import math
import numpy as np
import matplotlib.pyplot as plt

sceltaf = input("Scegli funzione ")
 
scelta_funzione = {
        '1': [lambda x: np.sin(x) - 2 * np.sin(2 * x), -math.pi, math.pi],
        '2': [lambda x: np.sinh(x), -2, 2],
        '3': [lambda x: np.abs(x), -1, 1],
        '4': [lambda x: 1 / (1 + x ** 2), -5, 5]
}

f, A, B = scelta_funzione.get(sceltaf)

n = int(input("Introduci il valore di n "))
step = (B-A)/(n+1)

#Costruisco n+1 punti equidistanti in [A,B), (l'estremo B viene quindi escluso)
x = np.arange(A,B,step)
#Mappo i punti dell'intervallo [A,B) in [l,r)  = [0,2pigreco)
l = 0
r = 2 * math.pi
# Settare il grado del polinomio trigonometrico "m"
if n % 2 == 0:
    m = n // 2 # Divisione intera (m deve essere intero)
else:
    m = (n - 1) // 2

# Valuto f in x  
y = f(x)

# Viene valutata in [0, 2PIG) a prescindere ma non i divide per n+1 (lo faccio a mano)
c = fft(y)
a = np.zeros((m + 2,))
b = np.zeros((m + 2,))
a0 = c[0]/(n + 1)
a[1 : m + 1] = 2 * c[1 : m + 1].real / (n + 1)    
b[1 : m + 1] = -2 * c[1 : m + 1].imag / (n + 1) 

if n % 2 == 0:
    a[m + 1] = 0
    b[m + 1] = 0
    
else:
    a[m + 1] = c[m + 1] / (n + 1) 
    b[m + 1] = 0
    
# vettore COLONNA [a0, ..., a0]
pol = a0 * np.ones((100, ))
z = np.linspace(A, B, 100 )
# Mappo i valori nel nuovo inervallo
zm = (z - A) * (r - l) / (B - A) + l

# Implemento la formula del polinomio trigonometrico
for k in range(1, m + 2):
   pol = pol + a[k] * np.cos(k * zm) + b[k] * np.sin(k * zm) # Focus

plt.plot(z,pol,'r',x  ,y ,'o',z ,f(z),'b')
plt.show()

