import pandas as pd

df = pd.read_csv('owid-covid-data.csv')


print(df.columns)

print(df.head())

print(df.isnull().sum())

countries = ['Kenya', 'United States', 'India']
df_filtered = df[df['location'].isin(countries)]

df_filtered['date'] = pd.to_datetime(df_filtered['date'])

df_filtered[['total_cases', 'total_deaths', 'total_vaccinations']] = df_filtered[
    ['total_cases', 'total_deaths', 'total_vaccinations']
].fillna(method='ffill')

