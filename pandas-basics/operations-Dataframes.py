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


#Showing people over 20 years old
print(df[df["age"] > 20])


print("----------------------------------")


#Showing people over 20 years old and male
print(df[(df["age"] > 20) & (df["gender"] == "male")])