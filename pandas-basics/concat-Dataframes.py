import numpy as np
import pandas as pd

data1 = {"name":     ["Gab"  , "Alex" , "Scarlet" , "stephania" , "John" ],
        "age":       [ 20    ,   25   ,    26     ,     35      ,   40   ],
        "gender":    ["male" , "male" , "female"  , "female"    , "male" ],
        "Insurance": [True ,  False ,   False   ,   True      ,  True    ] 
        }


data2 = {"col1": np.random.randint(0,10,size=10),
         "col2": np.random.randint(0,10,size=10)
         }


data3 = {"name":  ["Gab"  , "Alex" , "Scarlet" , "stephania" , "John" , "Max" , "Adam" ],
         "number": np.random.randint(0,10,size=7)
         }


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

print(df1)

print("------------------------------")

print(df2)

print("------------------------------")

print(df3)


print("------------------------------")

#It will concat df and df2 rows and columns
print(pd.concat([df1,df2]))

print("------------------------------")

#axis = 0 will concat rows and columns (by default axis is 0)
#axis = 1 will concat columns and rows and it puts joint indexes Next to each other. 
print(pd.concat([df1,df2], axis=1))


print("------------------------------")


#Inner join concats df1 and df2 and just show joint indexes
print(pd.concat([df1,df2] ,axis=1 , join="inner"))


print("------------------------------")

df1.set_index(["name"] , inplace=True)
df3.set_index(["name"] , inplace=True)


print(pd.concat([df1,df3] ,axis=1 , join="inner"))