# -*- coding: utf-8 -*-
"""
Esecizio 3
"""

from scipy.fft  import fft
import math
import numpy as np
 
import matplotlib.pyplot as plt
'''
Il problema fornisce n+1 (xi,yi), i=0,.n n=9 misurazioni del flusso sanguigno
attraverso una sezione dell’arteria carotide durante un battito cardiaco.---
ad istanti di tempo equistanti con step 1/10
Gli istanti appartengono all'intervallo [0,1)

'''

n=9;
A=0
B=1
l=0
r=2*math.pi

step=(B-A)/(n+1)
x=np.arange(A,B,step)
 
y =np.array([3.7, 13.5, 5, 4.6, 4.1, 4.5, 4, 3.8, 3.7, 3.7])

#Mappatura dell'intervallo [A,B) in [0,2*pigreco)

xm=(x-A)*(r-l)/(B-A)+l
 
if n%2==0:
    m=n//2
else:
    m=(n-1)//2


    
#Calcolo i coefficienti di Fourier della sequenza di dati y
c=fft(y)

#Da essi ricavo i coefficienti ak, k=0,..m+1 e bk, k=1,..m+1 della funzione trigonometrica interpolabnte
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
   
 
  
    