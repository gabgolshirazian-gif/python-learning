import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

arr = np.random.normal(size=100000)
plt.hist(arr , bins=100) 
plt.show()


mean = arr.mean()
std = arr.std()


up = mean + std
down = mean - std


up1 = mean + (2*std)
down1 = mean - (2*std)


#arr1 is between (mean + STD) and (mean - STD)
#the result is 68 % 
arr1 = arr[(arr > down) & (arr < up)]
print(((arr1.size) / 100000) * 100)


#arr2 is between (mean + 2STD) and (mean - 2STD)
#the result is 95 %
arr2 = arr[(arr > down1) & (arr < up1)]
print(((arr2.size) / 100000) * 100)








