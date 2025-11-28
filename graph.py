import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





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

def Func(z):
    return 18*z+400

fig = plt.figure()

ax = fig.add_subplot(111)

#df = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（工学部分光器U4000）/20240226/CSVデータ/spectraron.csv',encoding='shift_jis', header=None).iloc[350:1750]
#dx=func(df.index)
#dff= pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（オルフェス蛍光）/20240209 文化財/紙(UDS).csv',encoding='shift_jis', header=36)

df1 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/Rgunzyo2_divide_ratio.csv',encoding='shift_jis', header=None)
dx=func(df1.index)
dx1=Func(df1.iloc[0,:].values)
#for i in range(400,600):
#    df11=df1.iloc[i,:]
#    ax.plot(dx1,df11,c='blue')

df2 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/RFprussian1_divide_ratio.csv',encoding='shift_jis', header=None)
#df2ex = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/Rshu+white_EX_2ndDIV.csv',encoding='shift_jis', header=None)
dx2=Func(df2.iloc[0,:].values)
#dx2=df2.iloc[0,:].values
for i in range(df2.shape[0]-1):
    df22=df2.iloc[i+1,:].values
    ax.plot(dx2,df22,)
#ax.plot(dx2,df2.iloc[450,:].values,c='blue')

df3 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RSNVgunzyo2.csv',encoding='shift_jis', header=None)
dx3=Func(df3.iloc[0,:].values)
df3=df3.iloc[800,:].values
#ax.plot(dx3,df3, c='black')


#df4 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RFtouou_2ndDIV.csv',encoding='shift_jis', header=None)
#dx4=Func(df4.iloc[0,:].values)
#df4=df4.iloc[10,:].values
#ax.plot(dx4,df4, c='yellow')

#ax.plot(dx,df4/(2.75*df),c='blue', lw=1,label='phthalocyanine')


ax.set_xlabel('wavelength(nm)')
ax.set_ylabel('luminessence')
ax.set_title('indigo')
#ax.set_xlim(400,1100)
#ax.set_ylim(-0.25,0.25)
ax.legend()

plt.show()

