import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from statsmodels.api import qqplot


rand_normal = np.random.normal(size= 10000)


# In a uniform distribution, the data distribution is uniform
# and the probability of occurrence is the same.
rand_uniform = np.random.uniform(-3,3 , size= 10000)


sns.histplot(rand_normal , kde=True)
plt.show()


sns.histplot(rand_uniform , kde=True)
plt.show()


# In this plot our normal distribution is standard
qqplot(rand_normal , line='45')
plt.show()



# As the scale or STD increases, the Scattering of the data increases,
# resulting in our normal distribution moving away from the standard state.
rand_normal = np.random.normal(size= 10000 , scale= 5)
qqplot(rand_normal , line='45')
plt.show()



# In the uniform distribution, our distribution is in the shape of the letter s, 
# and in this case, our distribution is far from the normal distribution.
qqplot(rand_uniform , line='45')
plt.show()



# Comparison of normal and uniform distributions :
# In a normal distribution, our data tends toward the median, and in a uniform distribution,
# part of our data is toward the median. Therefore, the part of our plot that is in the
# shape of the letter S in a uniform distribution is a flat line.
rand_normal = np.random.normal(size= 10000)
plt.hist(rand_normal , bins=30)
plt.hist(rand_uniform , bins=30 , alpha = 0.5)
plt.show()
