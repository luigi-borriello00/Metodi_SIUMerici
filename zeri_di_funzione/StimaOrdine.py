# -*- coding: utf-8 -*-
"""
Stima ordine P
"""
import numpy as np

def stimaOrdine(xks, num_iterazioni):
    k = num_iterazioni - 3
    return np.log(abs(xks[k+2] - xks[k+3]) / abs(xks[k+1] - xks[k+2])) / np.log(abs(xks[k+1] - xks[k+2]) / abs(xks[k] - xks[k+1]))
