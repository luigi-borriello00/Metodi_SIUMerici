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

A=-3
B=3
l=0
r=2*math.pi

n = int(input("Introduci il valore di n "))
step = (B - A) / (n + 1)

#Costruisco n+1 punti equidistanti in [A,B), (l'estremo B viene quindi escluso)
x = np.arange(A,B,step)
#Mappo i punti dell'intervallo [A,B) in [0,2pigreco)
xm=(x-A)*(r-l)/(B-A)+l
 
if n%2==0:
    m=n//2
else:
    m=(n-1)//2

y=np.zeros((n+1,))
for i in range(0,n+1):
    y[i]=gradino(x[i])

c=fft(y)
a=np.zeros((m+2,))
b=np.zeros((m+2,))
a0= c[0]/(n+1)
a[1:m+1]=2*c[1:m+1].real/(n+1)    
b[1:m+1]=-2*c[1:m+1].imag/(n+1) 

if n%2==0:
    a[m+1]=0
    b[m+1]=0
    
else:
    a[m+1]=c[m+1]/(n+1) 
    b[m+1]=0
    
    
pol=a0*np.ones((100,))
z=np.linspace(A,B,100 )
zm=(z-A)*(r-l)/(B-A)+l


for i in range(1,m+2):
   pol= pol+a[i]*np.cos(i*zm)+b[i]*np.sin(i*zm)
   plt.plot(z,pol,'r',x  ,y ,'o')
   plt.show()
   
