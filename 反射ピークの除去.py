import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import os
import tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import sys
from sklearn import preprocessing

#任意のデータを取得
data0=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFfutarosianin3.csv',header=0)
#掛け算する意味ないかな
#任意の二次微分データを取得
data0_2ndDIV=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFfutarosianin3_2ndDIV.csv',header=None)
data0_2ndDIV=data0_2ndDIV.iloc[1:,:]
print(np.shape(data0_2ndDIV))
#二次微分データの負値は反射だからゼロにする

Data0=[]
for o in range(np.shape(data0_2ndDIV)[0]):
    for i in range(np.shape(data0_2ndDIV)[1]):
        if data0_2ndDIV.iloc[o,i]<0:
            Data0.append(0.0)
        else:
            Data0.append(data0_2ndDIV.iloc[o,i])

Data0=np.reshape(Data0,(int(np.shape(data0_2ndDIV)[0]),int(np.shape(data0_2ndDIV)[1])))
#data0=data0.iloc[5,:]
#data=data0*Data0
data=pd.DataFrame(Data0) #ここを変えたら負値にするか決めれる。今は負値なしで計算してる
for i in range(np.shape(data)[0]):
    plt.plot(data.iloc[i,:])
plt.show()


data.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/RFindasrin2_2ndDIV_analysis.csv',encoding='shift_jis')

Data1=[]
print(data.shape)
for o in range (int(np.shape(data)[0])):
    Max=pd.DataFrame(data.iloc[o,:]).values.max()
    for i in range(int(np.shape(data)[1])):
        data1=(data.iloc[o,i]/Max)
        Data1.append(data1)

Data1=np.reshape(Data1,(int(np.shape(data)[0]),int(np.shape(data)[1])))
data1=pd.DataFrame(Data1)
for i in range(np.shape(data1)[0]):
    plt.plot(data1.iloc[i,:])
plt.show()

data1.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/RFindasrin_2ndDIV_analysis_ratio.csv',encoding='shift_jis')
print((data0.iloc[10,10])*(data1.iloc[10,10]))
print(np.shape(data0))
print(np.shape(data1))
print(type(data0.iloc[10,10]))
Data0=[]
data0=pd.DataFrame(data0)
#for o in range(int(np.shape(data0)[0])):
#    min=data0.iloc[o,:].values.min()
#    for i in range(int(np.shape(data0)[1])):
#        data00=(data0.iloc[o,i] - min)
#        Data0.append(data00)
#data0=np.reshape(Data0,(int(np.shape(data0)[0]),int(np.shape(data0)[1])))
#data0=pd.DataFrame(data0)

Data0=[]
for o in range (int(np.shape(data0)[0])):
    Min=data0.iloc[o,:].values.min()
    for i in range(int(np.shape(data0)[1])):
        data00=(data0.iloc[o,i]/Min)
        Data0.append(data00)

Data0=np.reshape(Data0,(int(np.shape(data0)[0]),int(np.shape(data0)[1])))
data0=pd.DataFrame(Data0)

for i in range(np.shape(data0)[0]):
    plt.plot(data0.iloc[i,:])
plt.show()


Data2=[]
for o in range (data0.shape[0]):
    for i in range(data0.shape[1]):
        data2=(data1.iloc[o,i])/(data0.iloc[o,i])
        Data2.append(data2)
Data2=np.reshape(Data2,(int(np.shape(data0)[0]),int(np.shape(data0)[1])))
data2=pd.DataFrame(Data2)
for i in range(np.shape(data2)[0]):
    plt.plot(data2.iloc[i,:])
plt.show()

data2.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/RFfutarosianin3_divide.csv',encoding='shift_jis')

Data2=[]
for o in range (int(np.shape(data2)[0])):
    Max=pd.DataFrame(data2.iloc[o,:]).values.max()
    for i in range(int(np.shape(data2)[1])):
        data22=(data2.iloc[o,i]/Max)
        Data2.append(data22)

Data2=np.reshape(Data2,(int(np.shape(data2)[0]),int(np.shape(data2)[1])))
data2=pd.DataFrame(Data2)
for i in range(np.shape(data2)[0]):
    plt.plot(data2.iloc[i,:])
plt.show()

data2.to_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/CSVデータ/RFfutarosianin3_divide_ratio.csv',encoding='shift_jis')
