import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#the scores of students in Japan
a = np.random.randint(0,100,size=50)
#the scores of students in Iran
b = np.random.randint(0,20,size=60)


std_a = a.std()
mean_a = a.mean()

std_b = b.std()
mean_b = b.mean()


#calculating COV
a_cov = std_a / mean_a
b_cov = std_b / mean_b


print(a_cov)


print("-------------------------------")


print(b_cov)