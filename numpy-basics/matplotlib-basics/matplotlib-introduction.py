import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,10,1)
y = x**2


plt.plot(x,y)
plt.savefig("matplotlib-introduction.png")
plt.show()