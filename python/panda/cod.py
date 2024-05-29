import pandas as pd

# Reading data from a CSV file
df = pd.read_csv('data.csv')
print(df)


# Reading data from an Excel file
df = pd.read_excel('data.xlsx')
print(df)

# Reading data from a JSON file
df = pd.read_json('data.json')
print(df)
