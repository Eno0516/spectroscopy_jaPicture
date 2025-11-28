import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



fig = plt.figure()

ax = fig.add_subplot(111)

df = pd.read_csv('C:/Users/psaruv223/OneDrive - Osaka University/ドキュメント/修士（文化財）/計測結果（イメージング分光器）/20240226/CSVデータ/RSNVgunzyo2.csv',encoding='shift_jis', header=None)
df=pd.DataFrame(df)
df=pd.DataFrame(df.iloc[1:,0:].values,columns=df.iloc[0,0:].values)
for i in range (df.shape[0]):
    ax.plot(df.columns,df.iloc[i,:])
ax.set_title('Rbyakugun')
plt.show()
print(np.shape(df))

fig = plt.figure()
plt.plot(df.iloc[550,:])
plt.show()