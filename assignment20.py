#Q1
import pandas as pd
data={'Name':['jasleen','ginni','simran','rajat',],'Age':[20,22,21,20],'mail id':['jazz.k@gmail.com','ginni.j@gmail.com','rajat.b@gmail.com','simran.s@gmail.com'],'Phon Number':[9876543210,5647382910,2314567890,9078563412]}
df=pd.DataFrame(data)
print(df)

#Q2
import pandas as pd
data=pd.read_csv("datasheet.csv")
df=pd.DataFrame(data)
print(df)

print(df.head(5))

print(df.head(10))

print(df.shape)
print(df.axes)
print(df.sum())
print(df.describe())
print(df.size)
print(df.dtypes)

print(df.tail(5))

print("2nd column MinTemp:")
print(df['MinTemp'])
print(df['MinTemp'].shape)
print(df['MinTemp'].sum())
print(df['MinTemp'].describe())
print(df['MinTemp'].count())
print(df['MinTemp'].axes)
print(df['MinTemp'].mean())
print(df['MinTemp'].size)
print(df['MinTemp'].dtypes)
