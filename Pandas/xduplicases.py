import pandas as pd

m=pd.Series([1,2,3,4,5,3,23,41,23])
n=m.drop_duplicates()
print(n)