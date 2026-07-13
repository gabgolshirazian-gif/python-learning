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


df.set_index(["name"] , inplace=True)

#Drop : drop for deleting rows 
#axis = 0 (delete in row) , axis = 1 (delete in column)
df.drop(["John"] , axis=0 , inplace=True)
print(df)


print("----------------------------------")


#Another way in drop
df.drop(columns=["age"] , inplace = True)
print(df)


print("----------------------------------")


#Delete
del df["gender"]
print(df)


print("----------------------------------")


#Insert in Dataframes
df["age"] = [20,30,25,35]
print(df)


print("----------------------------------")


data1 = { "col1" : np.random.randint(0,10,size=10),
          "col2" : np.random.randint(0,10,size=10)
}

df_new = pd.DataFrame(data1)
print(df_new)


print("----------------------------------")


df_new["sum"] = df_new["col1"] + df_new["col2"]
print(df_new)