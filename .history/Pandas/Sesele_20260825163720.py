import pandas as pd

data = [10, 20, 30, 40]
labels = ['alpha', 'beta', 'gamma', 'delta']
s = pd.Series(data, index=labels)


vall = s.loc['beta']  


valp = s.iloc[1]        


val= s['beta']
print()
