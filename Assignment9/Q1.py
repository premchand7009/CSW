import numpy as np

x = np.linspace(0, np.pi, 10)
sine_values = np.sin(x)
cosine_values = np.cos(x)
sqrt_values = np.sqrt(x)

print("x values:       ", np.round(x, 4))
print("Sine values:    ", np.round(sine_values, 4))
print("Cosine values:  ", np.round(cosine_values, 4))
print("Square roots:   ", np.round(sqrt_values, 4))
