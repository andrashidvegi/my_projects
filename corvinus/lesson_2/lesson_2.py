import pandas as pd

df_prices = pd.read_csv('input/prices.csv')
df_prices_adjusted = pd.read_csv('input/prices-split-adjusted.csv')
df_securities = pd.read_csv('input/securities.csv')
df_fundamentals = pd.read_csv('input/fundamentals.csv')


def process_prices(df):
    df['date'] = df['date'].apply(lambda x: x[:10])
    df_filtered = df[['date', 'symbol', 'close']]
    df_pivot = pd.pivot_table(df_filtered, index=['date'], columns=['symbol'], values=['close'])
    df_pivot.columns = df_pivot.columns.droplevel()
    return df_pivot


df_prices_processed = process_prices(df_prices)
df_prices_adjusted_processed = process_prices(df_prices_adjusted)

def add_effective_returns(df):
    df_out = pd.DataFrame()
    for col in df.columns:
        df_out[col + '_effective_return'] = df[col] / df[col].shift(1) - 1
    return df_out

df_prices_processed_with_returns = add_effective_returns(df_prices_processed)
df_prices_adjusted_processed_with_returns = add_effective_returns(df_prices_adjusted_processed)

df_merged = df_prices_processed_with_returns.merge(
    df_prices_adjusted_processed_with_returns, on='date', suffixes=('_normal', '_adjusted'))

symbols = df_prices_adjusted_processed.columns

threshold_value = 0.001
splits = []
for symbol in symbols:
    df_symbol_returns = df_merged[[symbol + '_effective_return_normal', symbol + '_effective_return_adjusted']]
    df_split = df_symbol_returns.loc[
        df_symbol_returns[symbol + '_effective_return_normal'] -
        df_symbol_returns[symbol + '_effective_return_adjusted'] > threshold_value, ]
    if len(df_split > 0):
        splits.append(symbol + df_split.index[0])

print(splits)

# Processing: filter to needed cols, dates to datetime -> lambda

# pandas pivot to have it with symbols as columns

# To teach before:
# string replace with lambda
# groupby
# pivot table
