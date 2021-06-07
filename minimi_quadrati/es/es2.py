# -*- coding: utf-8 -*-
"""
Ese2
"""
import numpy as np
import matplotlib.pyplot as plt
from funzioni_Approssimazione_MQ import metodoQR

x = np.array([0.0004, 0.2507, 0.5008, 2.0007, 8.0013])
y = np.array([0.0007, 0.0162,0.0288, 0.0309, 0.0310]);

#Retta di regressione
n = 1
a = metodoQR(x,y,n)
residuo = np.linalg.norm(y-np.polyval(a,x))**2
print("Norma al quadrato del residuo Retta di regressione: {:e}" .format(residuo))
xval = np.linspace(np.min(x), np.max(x), 100)
pretta = np.polyval(a, xval)
plt.plot(xval,pretta,'-r',x,y,'o')

a = metodoQR(x,y,2)
residuo = np.linalg.norm(y-np.polyval(a,x))**2
print("Norma al quadrato del residuo Parabola di regressione: {:e}" .format(residuo))
xval = np.linspace(np.min(x), np.max(x), 100)
ppar = np.polyval(a, xval)
plt.plot(xval,ppar,'-g')

a = metodoQR(x,y,3)
residuo = np.linalg.norm(y-np.polyval(a,x))**2
print("Norma al quadrato del residuo Cubica di regressione: {:e}" .format(residuo))
xval = np.linspace(np.min(x), np.max(x), 100)
pcub = np.polyval(a, xval)
plt.plot(xval,pcub,'-y')

plt.legend(["Retta di regressione", "Parabola", "Cubica"])
plt.show()