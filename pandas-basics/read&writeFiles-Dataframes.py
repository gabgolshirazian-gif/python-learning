import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


btc_df = pd.read_csv("BTC-USD.csv")

print(btc_df.head())


print("-------------------------------")

btc_df.set_index("Date",inplace=True)
print(btc_df)


print("-------------------------------")


btc_open = btc_df["Open"]
plt.plot(btc_open)
plt.show()


print("-------------------------------")


#converting csv to xlsx
btc_df.to_excel("BTC_CH.xlsx")
df = pd.read_excel("BTC_CH.xlsx")
print(df)