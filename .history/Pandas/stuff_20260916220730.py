import pandas as pd


data = {
    'City': ['Toronto', 'Miami', 'Cairo', 'Tokyo'],
    'Temperature': [22.5, 31.0, 38.5, 26.0]  
}


df = pd.DataFrame(data)
print("--- Full Weather Data ---")
print(df)


highest_temp_index = df['Temperature'].idxmax()


hottest_city_row = df.loc[highest_temp_index]

print("\n--- Hottest City Details ---")
print(f"City: {hottest_city_row['City']}")
print(f"Temperature: {hottest_city_row['Temperature']}°C")
