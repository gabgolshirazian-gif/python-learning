import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns


data = pd.read_csv("student_data.csv")


print(data.head())


print("-------------------------------")


grade = data["G1"] + data["G2"] + data["G3"]
grade.hist(bins=50)
plt.show()


#Calculating skew (in this case skew is -0.14)
print(grade.skew())


#Calculating kurt (in this case kurt is -0.33)
print(grade.kurt())


sns.histplot(grade ,bins=50 , kde=True)
plt.show()



mean = grade.mean()
std = grade.std()


# If, in this example, we consider an incentive to increase students' scores and assume that
# students with a GPA below 43 have had an increase in GPA by STD/2, then the skewness and kurt
# situation is as follows:
grade[grade < 43] = grade[grade < 43] + (std/2) 



# As can be seen in the second plot, the skewness has shifted to the right, meaning that the 
#average score of students below 43 has increased, and so has kurt.
sns.histplot(grade ,bins=50 , kde=True)
plt.show()