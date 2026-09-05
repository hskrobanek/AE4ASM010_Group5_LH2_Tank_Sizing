import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 3

theta = np.linspace(0, 2*np.pi, 500)

x = b * np.cos(theta)
y = a * np.sin(theta)

plt.plot(x, y)
plt.axis("equal")
plt.grid(True)
plt.show()
