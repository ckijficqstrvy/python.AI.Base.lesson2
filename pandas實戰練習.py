import pandas as pd

df = pd.read_csv('data_DataFram.csv', index_col='data')
print(df)
print('--------------------------')
# 注意要保留索引值，記得用冒號來訪問
print(df.iloc[0:1])
print(df.iloc[:, 1:2])
print('--------------------------')
print(df.drop('2013-01-04'))
print('--------------------------')
#print(df.max(axis=1))
print(df.apply(lambda x: x.max(), axis=1))


