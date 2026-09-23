import pandas as pd

# Data for the cities
data = {
    'City': ['Toronto', 'Miami', 'Cairo', 'Tokyo'],
    'Temperature': [22.5, 31.0, 38.5, 26.0]  # Temperatures in Celsius
}

# Create the DataFrame
df = pd.DataFrame(data)
print("--- Full Weather Data ---")
print(df)

# Find the row index with the highest temperature
highest_temp_index = df['Temperature'].idxmax()

# Get the city details using the index row number
hottest_city_row = df.loc[highest_temp_index]

print("\n--- Hottest City Details ---")
print(f"City: {hottest_city_row['City']}")
print(f"Temperature: {hottest_city_row['Temperature']}°C")
