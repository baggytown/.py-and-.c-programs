import pandas as pd  # noqa: I001


data = {
    'Movie Name': ['Inception', 'The Dark Knight', 'Spirited Away', 'Toy Story'],
    'Genre': ['Sci-Fi', 'Action', 'Animation', 'Animation'],
    'Rating': [8.8, 9.0, 8.6, 8.3]
}


df = pd.DataFrame(data)
print(df)
