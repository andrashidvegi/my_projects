# Install pandas, numpy, matplotlib, openpyxl
import numpy as np
import pandas as pd

# Adatbeolvasas
df_voo = pd.read_csv('input/VOO.csv')
df_tlt = pd.read_csv('input/TLT.csv')

# Read test excel file, output to excel
# df_test = pd.read_excel('input/test.xlsx', sheet_name="Sheet1")
# df_test.to_excel('output/test_output.xlsx')
# print(df_test)
#
# # Dataframe letrehozas manualisan
df = pd.DataFrame(data={'A': [34, 2, 'b'], 'B': [3, 1, 131]})
# print(df)

# # print head, tail etc., evaluate/inspect in debug
# print(df_voo.head())
# print(df_voo.head(10))
# print(df_voo.tail(8))
# print(df_voo.columns)
# print(df_voo.index)
# print(df_voo.dtypes)
# print(df.dtypes)

# # Select / create / delete column
# print(df['A'])
# df['C'] = ''
# print(df)
# df['C'] = ['a', 'b', 'c']
# print(df)
# del df['C']
# print(df)

# df['A'] vs df[['A']] in debug


# print(df_voo.loc[10, 'Volume'])
# print(df_voo.loc[10, ])
# print(df_voo.loc[10])
#
# df_voo['Volume_in_thousands'] = df_voo['Volume'] / 1000
# df_voo['Ratio_of_open_close'] = df_voo['Open'] / df_voo['Close']

# print(df_voo)
#
# df_tlt_new = df_tlt.copy()
# df_tlt_new.index = df_tlt_new["Date"]
# del df_tlt_new['Date']
# print(df_tlt_new.iloc[0])
# print(df_tlt_new.iloc[-1])

# # merge: inner, left, right, outer
# df_merged = df_tlt.merge(df_voo, on='Date', suffixes=['_tlt', '_voo'], how='left')
#
# # print(df_merged)
#
# # Data cleaning
#
df_prop = pd.read_csv('../lesson_2/input/property data.csv')

print(df_prop.loc[df_prop["ST_NAME"] == 'LEXINGTON'])
msk = df_prop["ST_NAME"] == 'LEXINGTON'
print(df_prop.loc[msk])
print(df_prop.loc[df_prop["ST_NAME"] == 'LEXINGTON', "NUM_BATH"])
print(df_prop.loc[df_prop["ST_NAME"] == 'LEXIGTON', "NUM_BATH"])
# print(df_prop.loc[df_prop["ST_NAME"] == 'LEXINGTON', "NUM_ATH"])
# print(df_prop.loc[df_prop["ST_NAME"].isin(['LEXINGTON', "BERKELEY"])])
# print(df_prop.loc[(df_prop['ST_NUM'] < 200) & (df_prop['ST_NAME'] == 'LEXINGTON')])
#
# df_prop_notnull = df_prop.loc[df_prop['PID'].notnull()]
# print(len(df_prop), len(df_prop_notnull))
# df_prop = df_prop.rename(columns={"ST_NUM": "street_number", "ST_NAME": "street_name"})
# df_prop['PID'] = df_prop['PID'].fillna("X")
#
# df_voo['open_close_difference'] = df_voo['Close'] - df_voo['Open']
# for i, value in df_voo['open_close_difference'].iteritems():
#     if value < 0:
#         df_voo.loc[i, 'day_trend'] = 'negative'
#     elif value == 0:
#         df_voo.loc[i, 'day_trend'] = 'neutral'
#     else:
#         df_voo.loc[i, 'day_trend'] = 'positive'
#
# df_voo['effective_return'] = df_voo['Adj Close'] / df_voo['Adj Close'].shift(1) - 1
# df_voo['log_return'] = np.log(df_voo['Adj Close'] / df_voo['Adj Close'].shift(1))
# df_voo['cumsum_log_return'] = df_voo['log_return'].cumsum()
# print(np.exp(1.52894) * 80.74685)
# print('Daily expected logreturn: ', df_voo['log_return'].mean())
# print('Daily standard deviation: ', df_voo['log_return'].std(ddof=0))
# print('Yearly expected logreturn : ', 255 * df_voo['log_return'].mean())
# print('Yearly standard deviation: ', np.sqrt(255) * df_voo['log_return'].std(ddof=0))
#
# df_merged['log_return_tlt'] = np.log(df_merged['Adj Close_tlt'] / df_merged['Adj Close_tlt'].shift(1))
# df_merged['log_return_voo'] = np.log(df_merged['Adj Close_voo'] / df_merged['Adj Close_voo'].shift(1))
# df_merged_notnull = df_merged.loc[df_merged['log_return_voo'].notnull()]
# correlation = np.corrcoef(df_merged_notnull['log_return_tlt'], df_merged_notnull['log_return_voo'])
# df_merged_notnull['rolling_correlation'] = df_merged_notnull['log_return_tlt'].rolling(255).corr(
#     df_merged_notnull['log_return_voo'])
#
# df_ppp = pd.read_csv('input/ppp_data.csv')
# df_ppp.groupby('BorrowerState').count()
# print(pd.pivot_table(df_ppp, columns='ServicingLenderName', index='ProjectState', values='InitialApprovalAmount',
#                      aggfunc=np.sum))
import numpy as np
a = np.array([True, False])
b = np.array([False, False])

print (a | b)