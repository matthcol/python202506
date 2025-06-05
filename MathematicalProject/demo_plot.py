import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 6*np.pi, 1_000_000)
y = np.sin(x)
z = np.cos(x)

_ = plt.plot(x, y, x, z, linewidth=4)
plt.show()

