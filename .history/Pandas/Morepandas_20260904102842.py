import pandas as pd

# Create a Series with simple names and marks
x = pd.Series({
    'Alice': 85,
    'Bob': 35,
    'Charlie': 42,
    'David': 20,
    'Eve': 60,
    'Frank': 39,
    'Grace': 40
})

# Filter for 40 or above
y = x[x >= 40]

print(y)
