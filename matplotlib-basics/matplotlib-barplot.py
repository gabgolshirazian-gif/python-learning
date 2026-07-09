import numpy as np
import matplotlib.pyplot as plt

age = np.array([20,25,30,35,40,45])
AI_income = np.array([1000,1500,2000,2500,3000,3500])
DATA_income = np.array([1500,2000,2500,3000,3500,4000])

plt.bar(age,DATA_income, alpha= 0.5 , color = "blue" ,label = "DATA" , width= 3)
plt.bar(age,AI_income, alpha= 0.8 , color = "green" ,label = "AI", width = 3)
plt.savefig("matplotlib-barplot.png")
plt.legend()
plt.show()