import pandas as pd

file_name = './corona/2020-07.csv'
df =  pd.read_csv(file_name)
df_dates = pd.to_datetime(df['formatted_date'])
print('First: ', df_dates.min())
print('Last: ', df_dates.max())