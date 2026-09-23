import pandas as pd


data = {
    'Book Name': ['The Hobbit', '1984', 'To Kill a Mockingbird', 'The Great Gatsby'],
    'Author': ['J.R.R. Tolkien', 'George Orwell', 'Harper Lee', 'F. Scott Fitzgerald'],
    'Price':[]
}


df = pd.DataFrame(data)
print(df)
