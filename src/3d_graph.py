from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


ax = plt.axes(projection="3d")
#ax.scatter(3,5,7)
#plt.show()

#x_data = np.random.randint(0,100,(500,))
#y_data = np.random.randint(0,100,(500,))
#z_data = np.random.randint(0,100,(500,))

#ax.scatter(x_data,y_data,z_data)
#plt.show()


x_data = np.arange(-5,5,0.1)
y_data = np.arange(-5,5,0.1)
X , Y = np.meshgrid(x_data,y_data)
Z = np.sin(X) * np.cos(Y)

print(Z)
ax.plot_surface(X, Y, Z , cmap="plasma")
plt.show()


