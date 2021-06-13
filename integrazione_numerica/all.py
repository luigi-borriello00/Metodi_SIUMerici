# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 15:59:29 2021

@author: Luigi
"""
import numpy as np

def simpsonComp(fname, a, b, N):
    h = (b - a) / (2 * N)
    nodi = np.arange(a, b + h, h)
    f = fname(nodi)
    I = (f[0] + 2 * np.sum(f[2 : 2 * N : 2]) + 4 * np.sum(f[1 : 2 * N : 2]) + f[N * 2]) * h / 3
    return I

def trapeziComp(fname, a, b, N):
    h = (b - a) / (N)
    nodi = np.arange(a, b + h, h)
    f = fname(nodi)
    I = (f[0] + 2 * np.sum(f[1 : N]) + f[N]) * h / 2
    return I

def trapTol(fname, a, b, tol):
    NMAX = 2048
    err = 1
    N = 1
    IN = trapeziComp(fname, a, b, N)
    while N < NMAX and err > tol:
        N = N * 2
        I2N = trapeziComp(fname, a, b, N)
        err = abs(IN - I2N) / 3
        IN = I2N
        if N == NMAX:
            print("Raggiunto numero massimo di iterazioni")
            N = 0
            IN = []
            return IN, N
    return IN, N

def simpTol(fname, a, b, tol):
    err = 1
    N = 1
    In = simpsonComp(fname, a, b, N)
    NMAX = 2048
    while N < NMAX and err > tol:
        N = N * 2
        I2n = simpsonComp(fname, a, b, N)
        err = abs(In - I2n) / 15
        In = I2n
        if N == NMAX:
            print("Num. max di iterazioni raggiunto")
            N = 0
            In = []
            return In, N
    return In, N