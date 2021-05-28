import pandas as pd
import pandas_datareader as pdr
import sys
import matplotlib.pyplot as plt

print('Python: ' + sys.version.split('|')[0])
print('Pandas: ' + pd.__version__)
print('Pandas_datareader: ' + pdr.__version__)
print('Pandas_datareader:',pdr.__version__)

start = pd.to_datetime('2021-02-05')
end = pd.to_datetime('2021-04-05')
df = pdr.get_data_yahoo('WMT', start, end)
#print(df)
print(df.info())
m=df[['Open', 'Close']].plot(figsize=(15,5));
print(m)
