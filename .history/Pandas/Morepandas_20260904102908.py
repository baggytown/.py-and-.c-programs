import pandas as pd # type:ignore


x = pd.Series({
    'Alice': 85,
    'Bob': 35,
    'Charlie': 42,
    'David': 20,
    'Eve': 60,
    'Frank': 39,
    'Grace': 40
})


y = x[x >= 40]

print(y)
