import numpy as np
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
x_sample=[410,470,645,730,820,905,940]
y_sample=[160,264,600,768,936,1104,1176]

x_observed=[780,685,470,390]
y_observed=[1128,948,536,384]

plt.scatter(x_sample,y_sample)
plt.show()

x_sample=np.array(x_sample)
y_sample=np.array(y_sample)


def func(λ,L,b):
    a=1/L
    A=-a*a
    B=-2*a*b
    C=1-b*b
    N=1/(A*(λ**2)+B*λ+C)-1
    Z=L*((N)**0.5)
    return Z

L=5000
b=-0.3

#initial_parm=[L,a,b]

def func1(λ,L,A):
    return L*λ+A

def func2(λ,L,A):
    tan=np.tan(A*λ)
    return -L*tan

popt, pcov = curve_fit(func,x_sample,y_sample)


print(popt[0])
perr=np.sqrt(np.diag(pcov))
print(perr)

L=popt[0]
b=popt[1]
plt.plot(x_sample,func(x_sample,L,b))
plt.show()

