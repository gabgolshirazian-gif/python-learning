import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

data = pd.read_csv("student_data.csv")

grade = data["G1"] + data["G2"] + data["G3"]

# Q1 = 25 , Q2 = 32 , Q3 = 40
print(grade.describe())

data["ave"] = grade / 3 

# In the graph drawn for the columns ave, G1, G2, and G3, there is a rectangle
# for each box plot. The upper side is the value of Q3, the lower side is Q1, and
# the middle green line is Q2. For each of the columns G1, G2, and G3 and the
# value of ave, the degree of skewness and positive or negative skewness can be
# examined intuitively.
data.boxplot(["ave" , "G1" , "G2" , "G3"])
plt.show()