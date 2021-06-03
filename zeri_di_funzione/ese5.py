# -*- coding: utf-8 -*-
"""
Esercizio 5
"""
import numpy as np
import sympy as sym
import funzioni_zeri
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify

x0=2.5; 
tolx=1.e-8;
nmax=1000;

#Per la determinazione delle costanti c per cui il procedimento iterativo genera
#una successione convergente alla radice, cioè tali per cui |g'(alfa)|<1 analizzare
#su virtuale file pdf spiegazione teorica esercizio 5
c=[1/20, 1/6, 3/10, 2/5]
x=sym.symbols('x')
for j in range(4):
    gx= x-c[j]*(x**2-5)
    dgx=sym.diff(gx,x,1)
    g=lambdify(x,gx,np)
    dg=lambdify(x,dgx,np)
    x1,it,xk=funzioni_zeri.iterazione(g,x0,tolx,nmax)
   
    print('iterazioni= {:d}, soluzione={:e} \n\n'.format(it,x1))
    dgx1=abs(dg(x1))
    xx=np.linspace(1.5,3)
 

    plt.plot(xx,xx,'k-',xx,g(xx))
    plt.title("abs(g'(alfa))="+str(dgx1))
   
#Grafico della poligonale  
    Vx=[]
    Vy=[]
    for k in range(it):
        Vx.append(xk[k])
        Vy.append(xk[k])
        Vx.append(xk[k])
        Vy.append(xk[k+1])
    
    Vy[0]=0
    plt.plot(Vx,Vy,'r',xk,[0]*(it+1),'or-')

  
    plt.show()