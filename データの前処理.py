import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import os
import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import sys
from sklearn import preprocessing

#任意のデータをcsvから取得する

df1 = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/Fprussian4.csv',encoding='shift_jis', header=None)
data=pd.DataFrame(df1.iloc[1:,1:].values,index=df1.iloc[1:,0].values) #valuesにしないと上手く認識されないから気を付ける,400nm~1100nmの701個を扱う

#標準白色板のデータをcsvから取得し、有効な波長範囲で揃える
white=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/whitesample.csv',encoding='shift_jis',header=None)
white=pd.DataFrame(white.iloc[1:,1].values,index=white.iloc[1:,0].values)
print(data.iloc[0,0])
M=int(np.shape(data)[0]-1) #任意のデータの波長数-1 -1するのは、400~にしてるとスタートも含んでるから１波長分多くなってるため
N=int(np.shape(white)[0]-1) #標準白色版の波長数（こちらの方が多くなる）-1 -1するのは、400~にしてるとスタートも含んでるから１波長分多くなってるため
X=int(N/M) #白色と任意のデータ数比で任意データの波長の間隔がいくつか見る
DATA=[] 
for x in range (M+1): #任意のデータと波長範囲を揃える
   Data=0
   Data=white.iloc[X*x,0]
   DATA.append(Data)
white=pd.DataFrame(DATA) 
print(white)


DX=data.index #波長のデータ

#任意のデータを白色板のデータで割り反射率データを得る

DATA=[]
O=int(data.shape[0]) #波長
P=int(data.shape[1]) 
for p in range(P): 
   for o in range(O):
      Data=0
      data1=data.iloc[o,p] #p列のo行目（波長）
      white0=white.iloc[o,0]
      Data=data1/white0
      DATA.append(Data)
print(np.shape(DATA))
DATA=np.reshape(DATA,(P,O))
print(np.shape(DATA)) #(100,1024)で行ごとに位置のデータが来てる。最初と逆。for oの部分で列ごとに要素取って並べてるからそこで。

DATA_csv=pd.DataFrame(DATA,columns=DX)

#反射率データのグラフ化
fig = plt.figure()
ax = fig.add_subplot(111)
for p in range(P):
   ax.plot(DX,DATA_csv.iloc[p,:].values)
plt.show()
DATA_csv.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/RFprussian4.csv',index=False)



data=pd.DataFrame(DATA_csv.values,columns=DX)

#データを各サンプルa~b nmで正規化して前処理（ベースライン補正、多重散乱補正）したものをエクセルに保存
#ここでのa,bの範囲に基づいて正規化されるから、最もサンプル間で影響が少ないと思われる波長を選択しておく必要がある。
#xmin,xmax=550,600
#df=data.iloc[:,(xmin<data.columns)&(data.columns<xmax)]
#dff=pd.DataFrame(((data.T-df.T.min())/(df.T.max()-df.T.min())))
#dff=dff.T

#データを各サンプルでSNVして前処理（ベースライン補正、多重散乱補正）したものをエクセルに保存
snv=pd.DataFrame(preprocessing.scale(data,axis=1))
#print(np.shape(dff))

#SNV処理後の反射データのグラフ化

fig = plt.figure()
ax = fig.add_subplot(111)
for p in range(P):
   df=pd.DataFrame(snv)
   ax.plot(DX,df.iloc[p,:].values)
plt.show()

snv.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/RSNVFprussian4.csv',index=False)



fig = plt.figure()
bx = fig.add_subplot(111)

#それぞれの位置における反射データの二次微分データを関数近似から作成しエクセルに保存
DD=[]
for i in range (data.shape[0]):
   df1=data.iloc[i,:]
   window,polynom,order=5,2,0
   df1=signal.savgol_filter(df1,window,polynom,order)
   order=1
   df1=signal.savgol_filter(df1,window,polynom,order)
   order=0
   df1=signal.savgol_filter(df1,window,polynom,order)
   order=1
   df1=signal.savgol_filter(df1,window,polynom,order)
   DD.append(df1)
print(np.shape(DD))
DD=pd.DataFrame(DD)

#二次微分データのグラフ化
for i in range (np.shape(DD)[0]):
   bx.plot(DX,DD.iloc[i,:])

plt.show()

fig = plt.figure()
cx = fig.add_subplot(111)
cx.plot(DX,DD.iloc[10,:])
plt.show()

DD.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/RFprussian4_2ndDIV.csv',index=False)


sys.exit()



bx.plot(df1x,df1)

