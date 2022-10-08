import pandas as pd

df_prop = pd.read_csv('input/property data.csv')
df_prop['PID'] = df_prop['PID'].apply(lambda x: str(x)[:9])

df_test = pd.read_excel('input/pivot_data.xlsx')
df_pivot = pd.pivot_table(df_test, index=['Date'], columns=['Stock'], values=['Price'])
print(df_test.groupby('Stock').mean())
