import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


data = pd.read_csv("student_data.csv")


print(data.head())


print("-------------------------------")


df_grade = data["G1"] + data["G2"] + data["G3"]
print(df_grade.head())


print("-------------------------------")


#Calculating the mean
print(df_grade.mean())


print("-------------------------------")


#Calculating the median
print(df_grade.median())


print("-------------------------------")


#Calculating the mode (most repeated)
print(df_grade.mode())


print("-------------------------------")



#Calculating trim mean
print(stats.trim_mean(df_grade , 0.1))



print("-------------------------------")


#Calculating STD
print(df_grade.std())


print("-------------------------------")


len_g = len(df_grade)
mean = df_grade.mean()
median = df_grade.median()
mode = df_grade.mode()


plt.scatter(mean,1,s=500 , color = "r" )
plt.scatter(median,1,s=100 , color = "g" )
plt.scatter(mode,1,s=500 , color = "b" )


plt.show()

