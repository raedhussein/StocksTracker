import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf


data = yf.Ticker('BTC-USD')
x1 = data.history('7y')['Close'] 
plt.plot(x1, label='BTC')

data2 = yf.Ticker('AMZN')
x2 = data2.history('7y')['Close'] 
plt.plot(x2, label='AMZN')

data3 = yf.Ticker('GOOG')
x3 = data3.history('7y')['Close'] 
plt.plot(x3, label='GOOG')

data4 = yf.Ticker('VMW')
x4 = data4.history('7y')['Close'] 
plt.plot(x4, label="VMW")

data5 = yf.Ticker('MSFT')
x5 = data5.history('7y')['Close'] 
plt.plot(x5, label="MSFT")


plt.legend(loc="upper left")

plt.savefig('plot.png')
