import numpy as np
import matplotlib.pyplot as plt

plt.pie([100,80,50],labels=["Samsung","Apple","OnePlus"],colors=["r","g","b"],autopct="%.2f",startangle=-45,shadow=True,explode=(0,0,0.1))
plt.show()