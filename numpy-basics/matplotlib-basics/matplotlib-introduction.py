import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10,11,1)
y = x**2


plt.plot(x,y)
plt.savefig("matplotlib-introduction.png")
plt.show()


x = np.linspace(0,4*np.pi,100)
plt.plot(x,np.sin(x),label="sin",color= "red",linewidth = 3,linestyle = "--")
plt.plot(x,np.cos(x),label="cos",color="green",linewidth = 3,linestyle = "-.")
plt.savefig("matplotlib-sin&cos.png")
plt.title("sin&cos")
plt.xlabel("x")
plt.ylabel("x=sin , x=cos")
plt.grid(axis="both")
plt.legend()
plt.show()