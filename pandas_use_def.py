import pandas as pd
import numpy as np

arr = np.arange(16).reshape(4, 4)
df = pd.DataFrame(arr, ['a', 'b', 'c', 'd'],
                  ['A', 'B', 'C', 'D'])
print(df)
print('-----------------')

# apply是對每一列或行使用函數計算

print(df.apply(lambda x: x.std() - x.mean()))
print('---------')
print(df.apply(lambda x: x.max() - x.min(), axis=1))

# applymap是對每一個元素使用函數計算

print(df.applymap(lambda x: x + 10))
