import numpy as np
import matplotlib.pyplot as plt

plt.pie([100,80,50], labels=["Samsung","Apple","Oneplus"],autopct="%.2f" , colors=["r","g","b"], startangle=-45,explode=(0,0,0.1),shadow=True)
plt.show()