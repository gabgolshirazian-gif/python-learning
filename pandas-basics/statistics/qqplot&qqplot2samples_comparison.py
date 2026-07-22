import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from statsmodels.api import qqplot,qqplot_2samples


data = pd.read_csv("student_data.csv")

grade = data["G1"] + data["G2"] + data["G3"]
mean = grade.mean()
std = grade.std()


sns.histplot(grade ,bins=50 , kde=True)
plt.show()


# If, in this example, we consider an incentive to increase students' scores and assume that
# students with a GPA below 43 have had an increase in GPA by STD and students with a GPA above
# 43 have had an increase in GPA by STD/4 then the skewness and kurt
# situation is as follows:
grade_new = grade.copy()
grade_new[grade_new < 43] = grade_new[grade_new < 43] + std 
grade_new[grade_new > 43] = grade_new[grade_new > 43] + std/4

# As can be seen in the second plot, the skewness has shifted to the right, meaning that the 
# average score of students below 43 has increased, and so has kurt.
sns.histplot(grade_new ,bins=50 , kde=True)
plt.show()


# Checking grade with qqplot : as we can see in the output result grade distribution is normal
# distribution but it is far from standard normal distribution
qqplot(grade , line = '45')
plt.show()


# As we can see in this result plot in qqplot_2samples we are comapring grade and grade_new 
# as we can see students with GPA below 43 have had an increase in GPA by STD and the students
# with GPA above 43 have had an increase in GPA by STD/4
qqplot_2samples(grade,grade_new,line='45')
plt.show()