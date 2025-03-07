

#%load_ext autoreload
#%autoreload 2

import pandas as pd

df = pd.read_csv('NYPD_Hate_Crimes_20250131.csv')

#print(df)
print(df.describe())
print(df['Offense Category'].unique())

def remove_colour(data):
    no_color=df['Offense Category'] = df['Offense Category'].str.replace('Race/Color', 'Race')
    return no_color
