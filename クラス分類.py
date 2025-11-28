import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

data0=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RFfutarosianin_divide_ratio.csv',header=None)
DX=data0.iloc[0,1:]
data0=pd.DataFrame(data0.iloc[1:,1:].values)
data00=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFfutarosianin1_divide_ratio.csv',header=None)
data00=pd.DataFrame(data00.iloc[1:,1:].values)
data000=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFfutarosianin2_divide_ratio.csv',header=None)
data000=pd.DataFrame(data000.iloc[1:,1:].values)
data0000=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFfutarosianin3_divide_ratio.csv',header=None)
data0000=pd.DataFrame(data0000.iloc[1:,1:].values)
INDEX0=[0]*int(data0.shape[0]+data00.shape[0]+data000.shape[0]+data0000.shape[0])

data1=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RFgunzyo_divide_ratio.csv',header=None)
data1=pd.DataFrame(data1.iloc[1:,1:].values)
data11=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFgunzyo1_divide_ratio.csv',header=None)
data11=pd.DataFrame(data11.iloc[1:,1:].values)
data111=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFgunzyo2_divide_ratio.csv',header=None)
data111=pd.DataFrame(data111.iloc[1:,1:].values)
data1111=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFgunzyo3_divide_ratio.csv',header=None)
data1111=pd.DataFrame(data1111.iloc[1:,1:].values)
INDEX1=[1]*int(data1.shape[0]+data11.shape[0]+data111.shape[0]+data1111.shape[0])

data2=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RFindasrin_divide_ratio.csv',header=None)
data2=pd.DataFrame(data2.iloc[1:,1:].values)
data22=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFindasrin1_divide_ratio.csv',header=None)
data22=pd.DataFrame(data22.iloc[1:,1:].values)
data222=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFindasrin2_divide_ratio.csv',header=None)
data222=pd.DataFrame(data222.iloc[1:,1:].values)
data2222=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFindasrin3_divide_ratio.csv',header=None)
data2222=pd.DataFrame(data2222.iloc[1:,1:].values)
INDEX2=[2]*int(data2.shape[0]+data22.shape[0]+data222.shape[0]+data2222.shape[0])

#data3=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RFindigo_divide.csv',header=None)
#data3=pd.DataFrame(data3.iloc[1:,1:].values)
#INDEX3=[3]*int(data3.shape[0])

data4=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/RFprussian_divide_ratio.csv',header=None)
data4=pd.DataFrame(data4.iloc[1:,1:].values)
data44=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFprussian1_divide_ratio.csv',header=None)
data44=pd.DataFrame(data44.iloc[1:,1:].values)
data444=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFprussian2_divide_ratio.csv',header=None)
data444=pd.DataFrame(data444.iloc[1:,1:].values)
data4444=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFprussian3_divide_ratio.csv',header=None)
data4444=pd.DataFrame(data4444.iloc[1:,1:].values)
data44444=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240918/csvデータ/RFprussian4_divide_ratio.csv',header=None)
data44444=pd.DataFrame(data44444.iloc[1:,1:].values)
INDEX4=[4]*int(data4.shape[0])


INDEX=INDEX0+INDEX1+INDEX2+INDEX4
data=pd.concat([data0,data00,data000,data0000,data1,data11,data111,data1111,data2,data22,data222,data2222,data4])
print(np.shape(DX))
data=pd.DataFrame(data.values,index=INDEX,columns=DX)
print(data)
data.T.plot()
plt.show()
print(data.index.value_counts())

from sklearn.model_selection import train_test_split
train,test=train_test_split(data,train_size=0.6,random_state=1)
print('training data')
print(train.index.value_counts())
print('\ntest data')
print(test.index.value_counts())

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model=LinearDiscriminantAnalysis().fit(train.values,train.index)

i=0
print('prediction=',model.predict([test.iloc[i]])[0])
print('correct=',test.index[i])

from sklearn.metrics import confusion_matrix
print('calibration')
print(pd.DataFrame(confusion_matrix(train.index,model.predict(train.values))))
print('\nvaridation')
print(pd.DataFrame(confusion_matrix(test.index,model.predict(test.values))))

from sklearn.metrics import classification_report
print('calibration')
print(classification_report(train.index,model.predict(train.values)))
print('\nvaridation')
print(classification_report(test.index,model.predict(test.values)))

#Rgunzyo 450:550
#Rgunzyo2 400:600
#Rfish 500:700
#Rfish2 550:600

sample=pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/csvデータ/Rgunzyo_divide_ratio.csv',header=None)
sample=pd.DataFrame(sample)
print(sample)
sampleblue=sample.iloc[500:515,1:]
for i in range(sampleblue.shape[0]):
    print('prediction',model.predict([sampleblue.iloc[i]])[0])

SAMPLEX=[]
for i in range(sampleblue.shape[0]):
    sampleX=model.predict([sampleblue.iloc[i]])[0]
    SAMPLEX.append(sampleX)
print(SAMPLEX)
L=int(len(SAMPLEX))
F=int(SAMPLEX.count(0))
G=int(SAMPLEX.count(1))
D=int(SAMPLEX.count(2))
I=int(SAMPLEX.count(3))
P=int(SAMPLEX.count(4))
print('フタロシアニン',F/L)
print('群青',G/L)
print('インダスリン',D/L)
print('インディゴ',I/L)
print('プルシアン',P/L)