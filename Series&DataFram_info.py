import numpy as np
import pandas as pd

se = pd.Series(np.linspace(0, 9, 3), index=['one', 'two', 'three'])
arr = np.arange(16).reshape(4, 4)
df = pd.DataFrame(arr, ['a', 'b', 'c', 'd'], ['A', 'B', 'C', 'D'])
print(se)
print(se.axes)
print(df)
print(df.axes)
print(df.info())
