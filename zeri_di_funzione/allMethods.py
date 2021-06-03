# -*- coding: utf-8 -*-
"""
Tutti i moduli di zeri di funzione uniti per comodità

"""
import numpy as np
import math

def sign(x) : return math.copysign(1, x)

def bisezione(fname, a, b, tol):
    fa=fname(a)
    fb=fname(b)
    if sign(fa)==sign(fb):
        print("Metodo non iterabile ciacia ")
        return [], 0, []
    else:
        # Lista di iterazioni
        xks = []
        eps = np.spacing(1)
        it = 0
        # Numero massimo di iterazioni
        nMax = int(math.ceil(3.3 * math.log10((b-a)/tol)))
        while it < nMax and abs(b-a) >= tol + eps * max(abs(a), abs(b)):
            # Calcolo il k esimo X
            xk = a + ((b-a)/2)
            xks.append(xk)
            if(sign(xks[it]) == sign(a)):
                a = xks[it]
            elif(sign(xks[it]) == sign(b)):
                b = xks[it]
            # Ho trovato lo Zero
            elif(fname(xks[it]) == 0):
                break;
            it += 1
        return xk, it+1, xks

def regula_falsi(fname, a, b, tol, nMax):
    # A e B devono avere segni discordi
    if sign(fname(a)) == sign(fname(b)):
        print("Algoritmo non applicabile")
        return [], 0, []
    else:
        xks = []
        it = 0
        eps = np.spacing(1)
        fk = fname(a)
        while it < nMax and abs(b-a) >= tol + eps * max(abs(a), abs(b)) and abs(fk) >= tol:
            # Calcolo il nuovo punto Xk
            xk = a - fname(a) * ((b - a)/(fname(b) - fname(a)))
            xks.append(xk)
            fk = fname(xk)
            if sign(xks[it]) == sign(a):
                a = xks[it]
            elif sign(xks[it]) == sign(b):
                b = xks[it]
            elif fname(xks[it]) == 0:
                break;
            it += 1
        return xk, it+1, xks

def corde(fname, fpname, x0, tolx, tolf, nMaxIt ):
    xks = []
    it = 0
    m = fpname(x0)
    # decremento costante quindi
    d = fname(x0)/m
    x1 = x0-d
    xks.append(x1)
    it += 1
    while it < nMaxIt and abs(fname(x1)) >= tolf and abs(x1-x0) >= tolx * abs(x1):
        x0 = x1
        d = fname(x0) / m
        x1 = x0-d
        xks.append(x1)
        it += 1
        if it == nMaxIt:
            print("Raggiunto numero massimo di iterazioni")
    return xks[it-1], it, xks

def secanti(fname, x0, xm1, tolx, tolf, nMaxIt):
    xk = []
    it = 0
    m = (fname(x0) - fname(xm1)) / (x0 - xm1)
    d = fname(x0) / m
    xk.append(x0 - d)
    it += 1
    while it < nMaxIt and abs(fname(x0-d)) >= tolf and abs(d) >= tolx * abs(x0 - d):
        xm1 = x0
        x0 = x0 - d
        m = (fname(x0) - fname(xm1)) / (x0 - xm1)
        d = fname(x0) / m
        xk.append(x0 - d)
        it += 1
        if it == nMaxIt:
            print("Numero massimo it raggiunte ")
            return xk[it-1], it, xk
    return xk[it-1], it, xk

def newton(fname, fpname, x0, tolx, tolf, nMaxIt):
    xk = []
    it = 0
    if abs(fpname(x0)) <= np.spacing(1):
        print("Derivata nulla in x0")
        return [], 0, []
    else:
        d = (fname(x0)/ fpname(x0))
        x1 = x0 - d
        xk.append(x1)
        it += 1
        while it < nMaxIt and fname(x1) >= tolf and abs(d) >= tolx * abs(x1):
            x0 = x1
            if abs(fpname(x0)) <= np.spacing(1):
                print("Derivata nulla in x0")
                return xk[it], it, xk
            d = (fname(x0)/ fpname(x0))
            x1 = x0 - d
            xk.append(x1)
            it += 1
            if it == nMaxIt:
                print("Numero massimo di iterazioni raggiunto")
        return xk[it-1], it, xk

def newtonModificato(func, dfunc, x0, tolx, tolf, nMax, m):
    it = 0
    xk = []
    # Controllo Derivata
    if abs(dfunc(x0)) < np.spacing(1):
        print("Derivata nulla")
        return [], 0, []
    # xi = xim1 - d
    d = func(x0)/dfunc(x0)
    x1 = x0 - (d*m)
    xk.append(x1)
    it += 1
    while it < nMax and abs(func(x1)) >= tolf and abs(d) >= tolx * abs(x1):
        x0 = x1
        # Controllo Derivata
        if abs(dfunc(x0)) < np.spacing(1):
            print("Derivata nulla")
            return x0, it, xk
        d = func(x0)/dfunc(x0)
        x1 = x0 - (d*m)
        xk.append(x1)
        it += 1
        if it == nMax:
            print("Raggiunto nMax iterazioni")
    return x1, it, xk

def stimaOrdine(xks, num_iterazioni):
    k = num_iterazioni - 3
    return np.log(abs(xks[k+2] - xks[k+3]) / abs(xks[k+1] - xks[k+2])) / np.log(abs(xks[k+1] - xks[k+2]) / abs(xks[k] - xks[k+1]))
