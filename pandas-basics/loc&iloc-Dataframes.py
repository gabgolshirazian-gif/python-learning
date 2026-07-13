import numpy as np
import pandas as pd


data = {"name":     ["Gab"  , "Alex" , "Scarlet" , "stephania" , "John" ],
        "age":      [ 20    ,   25   ,    26     ,     35      ,   40   ],
        "gender":   ["male" , "male" , "female"  , "female"    , "male" ],
        "Insurance":[True ,  False ,   False   ,   True      ,  True    ] 
        }


df = pd.DataFrame(data)
print(df)


print("----------------------------------")


#loc:Display the desired index information
print(df.loc[3])


print("----------------------------------")


df.set_index(["name"] , inplace=True)
print(df.loc["Gab"])
print(df.loc[["Gab" , "Alex"]])
print(df.loc[["Gab" , "Alex"]]["age"])


print("----------------------------------")


#Making a new dataframe from df with optional columns
df2 = df[["age" , "Insurance"]]
print(df2)


print("----------------------------------")


#iloc : iloc is working with index number
print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[-1])