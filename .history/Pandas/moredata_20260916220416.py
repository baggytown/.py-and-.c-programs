import pandas as pd


data = {
    'Product Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [1200.00, 25.50, 45.00, 300.00],
    'Quantity': [10, 50, 35, 15]
}


df = pd.DataFrame(data)
print(df)
