import requests
import pandas as pd
import json

url = "http://universities.hipolabs.com/search?country=United+States"

response = requests.get(url).json()

df = pd.DataFrame(response)

print(df.head())

count_na = df.isna().sum()
print(count_na)

unique_names = df["name"].value_counts()

print(unique_names)

query_task = df.query("name == 'Purdue University'")
print(query_task)

print(df.iloc[:,[1,2]])

print(df.head(4))