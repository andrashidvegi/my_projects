import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://www.kaggle.com/datasets/dgawlik/nyse

df_prices = pd.read_csv('input/prices.csv')
df_prices_adjusted = pd.read_csv('input/prices-split-adjusted.csv')
df_securities = pd.read_csv('input/securities.csv')


def process_prices(df):
    df['date'] = df['date'].apply(lambda x: x[:10])
    df_filtered = df[['date', 'symbol', 'close']]
    df_pivot = pd.pivot_table(df_filtered, index=['date'], columns=['symbol'], values=['close'])
    df_pivot.columns = df_pivot.columns.droplevel()
    return df_pivot

def add_effective_returns(df):
    df_out = pd.DataFrame()
    for col in df.columns:
        df_out[col + '_effective_return'] = df[col] / df[col].shift(1) - 1
    return df_out

df_prices_processed = process_prices(df_prices)
df_prices_adjusted_processed = process_prices(df_prices_adjusted)

def find_splits():
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
            splits.append((symbol, df_split.index[0]))
    split_stocks = [i[0] for i in splits]
    print(df_securities.loc[df_securities['Ticker symbol'].isin(split_stocks), 'Security'])

# find_splits()

def find_highest_return_sector():
    return_dicts = {}
    for col in df_prices_adjusted_processed:
        time_length = len(df_prices_adjusted_processed.loc[df_prices_adjusted_processed[col].notnull(), col]) / 255
        stock_yearly_return = (df_prices_adjusted_processed[col].iloc[-1]
                               / df_prices_adjusted_processed[col].iloc[0]) ** (1 / time_length) - 1
        return_dicts[col] = stock_yearly_return
    df_filtered_security = df_securities[['Ticker symbol', 'Security', 'GICS Sector']]
    df_filtered_security['yearly_returns'] = df_filtered_security['Ticker symbol'].map(return_dicts)
    print(df_filtered_security.groupby('GICS Sector').mean())
    return return_dicts


return_dict = find_highest_return_sector()

df_med = df_prices_adjusted_processed[['EW', 'IDXX']]
df_med['log_return_ew'] = np.log(df_med['EW'] / df_med['EW'].shift(1))
df_med['log_return_idxx'] = np.log(df_med['IDXX'] / df_med['IDXX'].shift(1))
correlation = np.corrcoef(df_med['log_return_ew'][1:], df_med['log_return_idxx'][1:])
df_med['rolling_correlation'] = df_med['log_return_ew'].rolling(255).corr(
    df_med['log_return_idxx'])

ew_log_mean = 255 * df_med['log_return_ew'].mean()
ew_log_std = np.sqrt(255) * df_med['log_return_ew'].std(ddof=0)

idxx_log_mean = 255 * df_med['log_return_idxx'].mean()
idxx_log_std = np.sqrt(255) * df_med['log_return_idxx'].std(ddof=0)

df_med['cumsum_ew'] = df_med['log_return_ew'].cumsum()
df_med['cumsum_idxx'] = df_med['log_return_idxx'].cumsum()

rf = 0.02
sharpe_ew = (ew_log_mean - rf) / ew_log_std
sharpe_idxx = (idxx_log_mean - rf) / idxx_log_std
print(sharpe_ew)

df_med['cumsum_ew'].plot()
df_med['cumsum_idxx'].plot()
plt.savefig("ew_idxx_investment_comparison.pdf")
plt.show()
df_med['rolling_correlation'].plot()
plt.savefig("ew_idxx_rolling_comparison.pdf")
plt.show()
