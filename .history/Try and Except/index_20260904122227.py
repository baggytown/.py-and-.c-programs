import pandas as pd

data = [10, 20, 30]
labels = ['a', 'b', 'c']
s = pd.Series(data, index=labels)

# Display the index values
print(s.index)
# Output: Index(['a', 'b', 'c'], dtype='object')
