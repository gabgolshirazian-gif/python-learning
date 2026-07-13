import numpy as np 
import pandas as pd 


data = {"name":     ["Gab"  , "Alex" , "Scarlet" , "stephania" , "John" ],
        "age":      [ 20    ,   25   ,    26     ,     35      ,   40   ],
        "gender":   ["male" , "male" , "female"  , "female"    , "male" ],
        "Insurance":[True ,  False ,   False   ,   True      ,  True    ] 
        }

df = pd.DataFrame(data)
print(df)


print("---------------------------------------")


#ُُShowing start and stop indexes and steps
print(df.index)


print("---------------------------------------")


#Placing custom indexes
df2 = pd.DataFrame(data , index=np.arange(10,15))
print(df2)
df_new = pd.DataFrame(data , index=["row1" , "row2" , "row3" , "row4" , "row5"])
print(df_new)


print("---------------------------------------")


#Setting columns as index
df3 = pd.DataFrame(data)
df3.set_index(["name" , "age"] , inplace=True)
print(df3)