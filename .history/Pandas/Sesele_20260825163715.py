import pandas as pd

data = [10, 20, 30, 40]
labels = ['alpha', 'beta', 'gamma', 'delta']
s = pd.Series(data, index=labels)


vall = s.loc['beta']  


val_pos = s.iloc[1]        


val_bracket = s['beta']
print()
