import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin, label='Sine', color='blue', linestyle='-')
plt.plot(x, y_cos, label='Cosine', color='red', linestyle='--')
plt.title('Sine and Cosine Functions')
plt.xlabel('X-axis (radians)')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()