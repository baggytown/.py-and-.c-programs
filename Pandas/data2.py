import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['HR', 'IT', 'IT', 'Finance'],
    'Salary': [60000, 85000, 90000, 75000]
}


df = pd.DataFrame(data)
print(df)
