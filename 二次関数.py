import numpy as np
X1=608
Y1=532
X2=1644
Y2=1064
X3=1010
Y3=580

a=((Y1-Y2)*(X1-X3)-(Y1-Y3)*(X1-X2))/((X1-X2)*(X1-X3)*(X2-X3))
b=(Y1-Y2)/(X1-X2)-a*(X1+X2)
c=Y1-a*X1*X1-b*X1
dx=a*(1000)**2+b*(1000)+c
print(a,b,c)
print(dx)
