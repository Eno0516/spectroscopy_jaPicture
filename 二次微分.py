import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import sys

fig = plt.figure()

ax = fig.add_subplot(121)
bx=fig.add_subplot(122)

#波長軸を一次関数で計算
x_observed=[640,1592] #position
y_observed=[532,1064] #wavelength

A=np.array([[x_observed[0],1],[x_observed[1],1]])
B=np.array([y_observed[0],y_observed[1]])

solve=np.linalg.solve(A,B)
print(solve[1])
a=solve[0]
b=solve[1]

def func(x): #波長を計算する関数を定義しておく
    return a*x+b

#データの読み込み
df = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240208/CSVデータ/spectraron.csv',encoding='shift_jis', header=None).iloc[350:1750]
#dx=func(df.index)
#dff= pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（オルフェス蛍光）/20240209 文化財/紙(UDS).csv',encoding='shift_jis', header=36)

df1 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（工学部分光器U4000）/20240207NIRreflectance/白群３(UDS).csv',encoding='shift_jis', header=39).iloc[0:1146]
df1x=df1.iloc[:,0]
df1=df1.iloc[:,1]

#ax.plot(df1x,df1)

#d1x=df1x.iloc[0]

#df1xAve=[]
#for i in range (df1.shape[0]-10):
#    d1x=df1x[i:i+10]
#    d1xave=sum(d1x.values)/10
#    df1xAve.append(d1xave)


#df1=df1.iloc[:,1]
#df1Ave=[]
#for i in range (df1.shape[0]-10):
#    dff1=df1[i:i+10]
#    df1ave=sum(dff1)/10
#    df1Ave.append(df1ave)
#print(len(df1Ave))
#ax.plot(df1xAve,df1Ave)


window,polynom,order=51,2,0
df1=signal.savgol_filter(df1,window,polynom,order)
ax.plot(df1x,df1)
window=51
order=1
df1=signal.savgol_filter(df1,window,polynom,order)
#ax.set_xlim(700,800)
order=0
df1=signal.savgol_filter(df1,window,polynom,order)
order=1
df1=signal.savgol_filter(df1,window,polynom,order)

bx.plot(df1x,df1)
#bx.set_xlim(700,800)
#bx.set_ylim(-0.003,0.001)

plt.show()


sys.exit()

df2 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（工学部分光器U4000）/20240207NIRreflectance/群青(UDS).csv',encoding='shift_jis', header=39)
df2x=df2.iloc[:,0]
df2=df2.iloc[:,1]
df3 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/byakugan.csv',encoding='shift_jis', header=None).iloc[350:1750]
dx=func(df3.index)
df3=df3/(2.9*df)
df3=df3.values[:,0] #shapeみたら.valuesだけやと列も含まれてた。ほしいのは配列のみ
df4 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/gunzyo.csv',encoding='shift_jis', header=None).iloc[350:1750]
df4=df4/(2.75*df)
df4=df4.values[:,0]
print(np.shape(df1))
print(np.shape(df3))
ax.set_xlabel('wavelength(nm)')
ax.set_ylabel('reflectance secder')
#ax.set_xlim(350,1850)
#ax.set_ylim(5,25)
ax.legend()

window,polynom,order=7,2,0
df1=signal.savgol_filter(df1,window,polynom,order)
order=1
df1=signal.savgol_filter(df1,window,polynom,order)
order=0
df1=signal.savgol_filter(df1,window,polynom,order)
order=1
df1=signal.savgol_filter(df1,window,polynom,order)

window,polynom,order=7,2,0
df2=signal.savgol_filter(df2,window,polynom,order)
order=1
df2=signal.savgol_filter(df2,window,polynom,order)
order=0
df2=signal.savgol_filter(df2,window,polynom,order)
order=1
df2=signal.savgol_filter(df2,window,polynom,order)

ax.plot(df1x,df1, c='red', lw=1,label='byakugun')
ax.plot(df2x,df2, c='blue', lw=1,label='gunzyou')
ax.set_xlim(700,800)
ax.set_ylim(-0.01,0.01)
bx.plot(df1x,df1, c='red', lw=1,label='byakugun')
bx.plot(df2x,df2, c='blue', lw=1,label='gunzyou')
plt.show()

window,polynom,order=31,2,0
df3=signal.savgol_filter(df3,window,polynom,order)
order=1
df3=signal.savgol_filter(df3,window,polynom,order)
order=0
df3=signal.savgol_filter(df3,window,polynom,order)
order=1
df3=signal.savgol_filter(df3,window,polynom,order)

window,polynom,order=31,2,0
df4=signal.savgol_filter(df4,window,polynom,order)
order=1
df4=signal.savgol_filter(df4,window,polynom,order)
order=0
df4=signal.savgol_filter(df4,window,polynom,order)
order=1
df4=signal.savgol_filter(df4,window,polynom,order)

fig = plt.figure()

ax = fig.add_subplot(121)
bx=fig.add_subplot(122)

ax.set_xlabel('wavelength(nm)')
ax.set_ylabel('reflectance secder')
#ax.set_xlim(350,1850)
#ax.set_ylim(5,25)
ax.legend()
ax.plot(dx,df3, c='red', lw=1,label='byakugun')
ax.plot(dx,df4, c='blue', lw=1,label='gunzyou')
ax.set_xlim(700,800)
bx.plot(dx,df3, c='red', lw=1,label='byakugun(imaging)')
bx.plot(dx,df4, c='blue', lw=1,label='gunzyo(imaging)')

plt.show()
