import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,10,1)
y = x**2


plt.plot(x,y)
plt.savefig("matplotlib-introduction.png")
plt.show()


x = np.linspace(0,4*np.pi,100)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.savefig("matplotlib-sin&cos.png")
plt.show()