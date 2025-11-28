import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import os
import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import sys
from scipy import interpolate as ip

#yを決定
#イメージング分光器のスリット幅から波長分解能を計算してyを決定

y=8 #波長


#標準白色板のデータを取得
idir=os.path.abspath(os.path.dirname('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226'))
root=tkinter.Tk()
root.attributes('-topmost',True)
root.withdraw()
tkinter.messagebox.showinfo('開きたいtif','開きたいtifを選択してください')
sample=tkinter.filedialog.askopenfilename(filetypes=[('TIFF files','*.tif')])
imagee=np.array(Image.open(sample))
white=pd.DataFrame(imagee) #whiteに元データを格納
print(np.shape(white))

#標準白色版の平均反射データをCSVファイルから取得
#white = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/spectraron.csv',encoding='shift_jis', header=None)

#データを波長分解能y行ずつで合わせて平均しその値を代表値とするデータセットWWを作成

x=int(4)
YY=[]
AA=[]
O=int(imagee.shape[0]/y)
I=int(imagee.shape[1]/x)
a=0
b=0
for o in range (O):
    a=a+1
    for i in range (I):
        b=b+1
        S=np.matrix(imagee[y*o:y*o+y,x*i:x*i+x]) #x×yの行列に
        OO=[]
        for n in range (S.shape[0]): #計算できるよう一列の配列に
         for m in range (S.shape[1]):
          d=S[n,m]
          OO.append(d)
        df=pd.DataFrame(OO)
        Q1=np.percentile(df.values,25)
        Q3=np.percentile(df.values,75)
        IQR=Q3-Q1
        A=Q1-1.5*IQR #外れ値の定義
        B=Q3+1.5*IQR
        data=df.iloc[(A<=df.values)&(df.values<=B),:] #外れ値の除外
        ave=sum(data.values)/len(data)
        AA.append(ave)
#print(np.shape(AA))
YY=np.reshape(AA,(a,int(b/a))) #要素をx×y行列に変換
print(np.shape(YY))
df=pd.DataFrame(YY)

#一度にやると上手く計算されなかったから残りを平均
DF=[]
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(df.shape[0]):
   df=pd.DataFrame(YY)
   df=sum(df.iloc[i,:].values)/df.shape[1]
   DF.append(df)
ax.plot(DF)
plt.show()

white=pd.DataFrame(DF) #平均化したデータをwhiteに格納

#波長関数を一次関数で定義

x_observed=[640,1592] #position
y_observed=[532,1064] #wavelength

A=np.array([[x_observed[0],1],[x_observed[1],1]])
B=np.array([y_observed[0],y_observed[1]])

solve=np.linalg.solve(A,B)
print(solve[1])
a=solve[0]
b=solve[1]

def func(z): #波長を計算する関数を定義しておく
    return a*z+b

#y行から波長変換DXを作成
#平均化しているから行ピクセルも平均化
dx=np.arange(2048)
dxm=dx[:y].mean()
dxM=dx[-y:].mean()
dx=np.arange(dxm,dxM+y,y)
print(dx)
DX=func(dx)
print(DX)

#3次スプライン補完によりデータの間隔を増やし波長が整数値となるデータセットを取得、有効範囲の400~1100nm±50nmで1 nm刻みでエクセルに保存する。

data=pd.DataFrame(white.values,index=DX)
xmin=350
xmax=1150
x,y=data.index,data.values
xdiv=1 #波長分解能と合わせるべき？
ix=np.arange(xmin,xmax+xdiv,xdiv)
iy=ip.interp1d(x,y,kind="cubic",axis=0)(ix)
Data=pd.DataFrame(iy)
data=pd.DataFrame(Data.values,index=ix)
plt.plot(data)
plt.show()

data.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/whitesample.csv',encoding='shift_jis')
