import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,np.pi,100)

fig = plt.figure(figsize=(8,8))

plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)

plt1.plot(x,np.sin(x),label= "sin" )
plt1.set_title("sin")

plt2.plot(x,np.cos(x),label= "cos" )
plt2.set_title("cos")

plt3.scatter(x[:10],np.sin(x)[:10],label= "sin" )
plt3.set_title("10 sinuses")


plt4.plot(x,np.tan(x),label= "tan" )
plt4.set_title("tan")

plt1.legend()
plt2.legend()
plt3.legend()
plt4.legend()

fig.subplots_adjust(hspace=0.5,wspace=0.5)
plt.show()