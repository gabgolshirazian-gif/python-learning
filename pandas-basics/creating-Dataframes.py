import numpy as np
import pandas as pd

data = {"col1":["a","b","c"],
        "col2":[1,2,None],
        "col3":[20,30,None]}

df = pd.DataFrame(data)
print(df)


print("--------------------------------------")


data2 = np.arange(1,7 , dtype=np.int8).reshape(2,3)
df2= pd.DataFrame(data2,columns=["a","b","c"])
print(df2)

print("--------------------------------------")

big_data = np.arange(200).reshape(100,2)
df_big = pd.DataFrame(big_data, columns=["col1" , "col2"])
print(df_big)

print("--------------------------------------")

big_data2 = np.arange(201).reshape(67,3)
df_big2 = pd.DataFrame(big_data2, columns=["col1" , "col2" , "col3"])
print(df_big2)

print("--------------------------------------")


#showing first 15 rows
print(df_big.head(15))
print(df_big2.head(15))


print("--------------------------------------")


#showing last 10 rows
print(df_big.tail(10))
print(df_big2.tail(10))