import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

for city in CITY_DATA:
    df = pd.read_csv(CITY_DATA[city])
    print(df.info())