# -*- coding: utf-8 -*-
"""
Created on Sat May  1 08:47:46 2021

@author: damia
"""
import numpy as np
import scipy.linalg as spl
from funzioni_Sistemi_lineari import Usolve
 
def metodoQR(x,y,n):
    """
    INPUT
    x vettore colonna con le ascisse dei punti
    y vettore colonna con le ordinate dei punti 
    n grado del polinomio approssimante
    OUTPUT
     a vettore colonna contenente i coefficienti incogniti
 """
 
    H=np.vander(x,n+1)
    Q,R=spl.qr(H)
    y1=np.dot(Q.T,y)
    a,flag=Usolve(R[0:n+1,:],y1[0:n+1])
    return  a

