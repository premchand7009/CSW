import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1, 2])
v2 = np.array([2, 1])

v1 = v1 / np.linalg.norm(v1)
v2 = v2 / np.linalg.norm(v2)

origin = [0, 0]

plt.quiver(*origin, v1[0], v1[1], color='green', angles='xy', scale_units='xy', scale=1, label='v1')
plt.quiver(*origin, v2[0], v2[1], color='red', angles='xy', scale_units='xy', scale=1, label='v2')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Normalized Vectors from Origin')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
