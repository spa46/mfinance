import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

import yfinance as yf

yf.pdr_override() # <== that's all it takes :-)

# pandas configuraiton
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

plt.style.use('dark_background')

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-01-10")
print(data)


data['Adj Close'].plot()

plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("Miscrosoft Price data")
# plt.show()

msft_daily_returns = (data['Adj Close'] / data['Adj Close'].shift(1)) - 1
print(data['Adj Close'].shift(1))
# print(msft_daily_returns))