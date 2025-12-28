import matplotlib.pyplot as plt
import numpy as np

x1=[0.4, 0.6, 0.5, 0.4, 0.6, 0.4]
x2=[-0.4, -0.6, -0.5, -0.4, -0.6, -0.4]
y=[0.8, 0.8, 0.0, -0.8, -0.8, 0.8]

plt.plot(x1, y, color='green')
plt.plot(x2, y, color='orange')
plt.show()