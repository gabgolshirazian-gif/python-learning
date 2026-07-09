import numpy as np
import pandas as pd


data = pd.Series(np.array([1,2,3] , dtype=np.int8))
print(data)

print("---------------------------------")

s = {"a":1,"b":2,"c":3}
data1=pd.Series(s)
print(data1)

print("---------------------------------")

s1 = pd.Series([1,2,3])
s2 = pd.Series(["a","b","c"])
df = pd.DataFrame([s1,s2])
print(df)

print("---------------------------------")

#showing s1 , s2 as column
data = {"col1":s1,"col2":s2}
df1 = pd.DataFrame(data)
print(df1)

print("---------------------------------")

#editing Dataframes(adding columns)
df_n = pd.DataFrame()
df_n["a"] = s1
df_n["b"] = s2
print(df_n)