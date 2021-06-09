# -*- coding: utf-8 -*-
"""
Interpolazione numerica in base di Lagrange

Pn = sommatoria di j = 0 -> yj * Lj
"""
import numpy as np
import math

"""
    np.poly() -> dato un vettore es [2,3] restituisce (x-2)(x-3) 

"""
def polinomioLagrange(xnodi, i):
    n = xnodi.size
    xzeri = []
    if i == 0:
        xzeri = xnodi[1:n]
    else:
        xzeri = np.append(xnodi[:i], xnodi[i + 1:n])                    
    num = np.poly(xzeri)
    den = np.polyval(num, xnodi[i])
    return num/den

"""
    Devo restituire le varie approssimazioni
    mi costruisco L = [L0(x0), ..., L0(xn)]
                      [...,     ...       ]
                      [Ln(x0), ..., Ln(xn)]
                      
    Avendo poi y della forma y = [y0, ..., yn]
    facendo y[:] * L[ : , k] ottengo Pn(k)

"""
def interpolL(x, y, xx):
    """"
        %funzione che determina in un insieme di punti il valore del polinomio
        %interpolante ottenuto dalla formula di Lagrange.
        % DATI INPUT
        %  x  vettore con i nodi dell'interpolazione
        %  f  vettore con i valori dei nodi 
        %  xx vettore con i punti in cui si vuole calcolare il polinomio
        % DATI OUTPUT
        %  y vettore contenente i valori assunti dal polinomio interpolante
        %
     """
    m = x.size
    n = xx.size
    somma = 0
    L = np.zeros((m,n))
    for i in range(n):
        L[i, :] = np.polyval(polinomioLagrange(x, i), xx)
    return np.dot(y,L)

"""
    Nodi di Chebishev
"""
def zeri_Cheb(a,b,n):
    t1=(a+b)/2
    t2=(b-a)/2
    x=np.zeros((n+1,))
    for k in range(n+1):
        x[k]=t1+t2*np.cos(((2*k+1)/(2*(n+1))*math.pi))

    return x