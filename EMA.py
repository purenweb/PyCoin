import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
stockValues = pd.DataFrame(
    {'Stock_Values': [60, 102, 103, 104, 101,
                      105, 102, 103, 103, 102]})

# finding EMA
# use any constant value that results in
# good smoothened curve
ema = stockValues.ewm(com=0.4).mean()

# Comparison plot b/w stock values & EMA
plt.plot(stockValues, label="Stock Values")
plt.plot(ema, label="EMA Values")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()