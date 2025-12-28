import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 25, 100)

y1 = x**3 - 15*x**2 + 25
y2 = 2*x**2 - 10*x + 5

plt.plot(x, y1, color='blue', linestyle='-', linewidth=2, label='L2: y = x³ - 15x² + 25')

plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='L3: y = 2x² - 10x + 5')

plt.title('Polynomial Curves Using NumPy and Matplotlib')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.grid(True)
plt.show()
