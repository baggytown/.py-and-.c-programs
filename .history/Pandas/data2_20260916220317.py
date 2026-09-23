import pandas as pd

# Data for the employees
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['HR', 'IT', 'IT', 'Finance'],
    'Salary': [60000, 85000, 90000, 75000]
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)
