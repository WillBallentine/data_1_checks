import requests
import pandas as pd
import json

url = "http://universities.hipolabs.com/search?country=United+States"

response = requests.get(url).json()

df = pd.DataFrame(response)

fixed_columns = {
    'web_pages': 'website',
    'state-province': 'state/province',
    'alpha_two_code': 'alpha code'
}

df.rename(columns=fixed_columns, inplace=True)
print(df.columns)


print(df.isnull())

df = df.fillna(value='NONE')

print(df)
