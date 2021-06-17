# -*- coding: utf-8 -*-
"""
es2 Parte 1
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def succU(n):
    s = []
    s.append(1)
    s.append(1 + (1/4))
    u = []
    u.append(1)
    u.append(1 + (1/4))
    for ni in range(2, n):
        s.append(s[ni - 1] + 1/((ni + 1)**2))
        u.append(math.sqrt(6 * s[ni]))
    return u



def succZ(n):
    z = []
    z.append(1)
    z.append(2)
    for ni in range(2, n):
        z.append((2**(ni - 0.5)) * math.sqrt(1 - (math.sqrt(1 - 4**(1-ni) * z[ni-1]**2))))
    return z

def succY(n):
    y = []
    y.append(1)
    y.append(2)
    for ni in range(2, n):
        num = (2**(ni - 0.5)) * math.sqrt((4**(1-ni)) * y[ni-1]**2)
        den = math.sqrt(1 + (math.sqrt(1 - 4**(1-ni) * y[ni-1]**2)))
        y.append(num / den)
    return y

u = np.array(succU(41))
z = np.array(succZ(41))
y = np.array(succY(41))

pi = np.ones((41,)) * math.pi

errRelU = np.abs(u - pi) / np.abs(pi)
errRelZ = np.abs(z - pi) / np.abs(pi)
errRelY = np.abs(y - pi) / np.abs(pi)
xx = np.arange(1,42)

plt.semilogy(xx, errRelU, xx, errRelZ, xx, errRelY)
plt.legend(["ErrRelU", "ErrRelZ", "ErrY"])
plt.show()



