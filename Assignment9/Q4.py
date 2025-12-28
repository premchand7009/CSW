import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 50)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.plot(x, y1, label='Sine')
plt.plot(x, y2, label='Cosine')
plt.plot(x, y3, label='Tangent')

plt.xlabel("x values")
plt.ylabel("Function value")
plt.title("Sine, Cosine and Tangent Curves")
plt.legend()
plt.show()
