import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import os
import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import sys
from scipy import interpolate as ip



#x,yを決定
#イメージング分光器のスリット幅から波長分解能を計算してyを決定 ※データのピクセル数を割り切れる数値にする
y=30 #波長

#空間分解能の要求値からxを決定 ※データのピクセル数を割り切れる数値にする
x=2 #位置

#任意のデータを取得

idir=os.path.abspath(os.path.dirname('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918'))
root=tkinter.Tk()
root.attributes('-topmost',True)
root.withdraw()
tkinter.messagebox.showinfo('開きたいtif','開きたいtifを選択してください')
sample=tkinter.filedialog.askopenfilename(filetypes=[('TIFF files','*.tif')])
imagee=np.array(Image.open(sample)) #任意のデータをimageeに格納

#imagee=np.array([[1,2,3,4],[5,50,7,8],[9,10,11,12],[13,14,15,16]]) #サンプル行列4×4を作成


#データをx×yのデータ群に分割して平均し、その値を代表値とするデータセットを作成しエクセルに保存

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
        ave=np.sum(data.values)/len(data)
        AA.append(ave)
#print(np.shape(AA))
YY=np.reshape(AA,(a,int(b/a))) #要素をx×y行列に変換
sample=pd.DataFrame(YY)

#１セルに行分全てのデータが入っちゃって上手くいかんかった。
#import csv
#f = open('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/分割byakugun.csv', 'w',newline='')
#I=int(np.shape(DATA)[0])
#O=int(np.shape(DATA)[1])
#for i in range(I):
#    for o in range(O):
#        data = [DATA[i,o]]
#        writer = csv.writer(f)
#        writer.writerow(data) 
#f.close()

#波長関数を一次関数で定義

x_observed=[412,1448] #position
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
dx=np.arange(2040) #波長データの総数に合わせる
dxm=dx[:y].mean()
dxM=dx[-y:].mean()
dx=np.arange(dxm,dxM+y,y)
print(dx)
DX=func(dx)
print(DX)

#有効ピクセルyを有効波長Yに変換

Y=round(a*y)
Y=18 #標準データの分解能に合わせた。ただここはデータによってまちまちだから自動化したいが、最終的には揃っていないとクラス分類が出来ないので、クラス分類前にデータを整理するのもアリだが、そうすると３次スプライン補完をもう一度する必要があるので何とも言えない

#以下に続くスプライン補完でデータ間隔を波長分解能に合わせるために
#3次スプライン補完によりデータの間隔を増やし波長が整数値となるデータセットを取得、有効範囲の400~1100nmで波長分解能のx nm刻みでエクセルに保存する。

data=pd.DataFrame(sample.values,index=DX)
xmin=400
xmax=1100
x,y=data.index,data.values
xdiv=int(Y) #波長分解能と合わせるべき
ix=np.arange(xmin,xmax+xdiv,xdiv)
iy=ip.interp1d(x,y,kind="cubic",axis=0)(ix)
Data=pd.DataFrame(iy)
data=pd.DataFrame(Data.values,index=ix)
plt.plot(data)
plt.show()

data.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/Ffutarosianin1.csv',encoding='shift_jis')








