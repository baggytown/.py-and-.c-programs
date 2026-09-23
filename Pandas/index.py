import pandas as pd

data = [10, 20, 30]
labels = ['a', 'b', 'c']
s = pd.Series(data, index=labels)


print(s.index)
