# -*- coding: utf-8 -*-
"""
Metodo QR

"""
import numpy as np
import funzioni_Sistemi_lineari as fz
import scipy.linalg as spl

"""
    INPUT: x vettore colonna con ascisse dei punti
            y vettore colonna con ordinate dei punti
            n grado del polinomio
    OUTPUT: a vettore colonna contenente coefficenti incogniti
"""
def metodoQR(x,y,n):
    # Matrice di Vandermond
    H = np.vander(x, n+1)
    Q,R = spl.qr(H)
    y1 = np.dot(Q.T, y)
    a, flag = fz.Usolve(R[:n+1,:], y1[:n+1])
    return a
