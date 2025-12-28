import numpy as np

angles_deg = np.array([0, 30, 45, 60, 90])

angles_rad = np.deg2rad(angles_deg)

sin_values = np.sin(angles_rad)
cos_values = np.cos(angles_rad)
tan_values = np.tan(angles_rad)

print("Angle(deg)\tRadians\tSin\tCos\tTan")
print("-" * 50)

for i in range(len(angles_deg)):
    print(f"{angles_deg[i]:>5}\t\t"
          f"{angles_rad[i]:.4f}\t"
          f"{sin_values[i]:.4f}\t"
          f"{cos_values[i]:.4f}\t"
          f"{tan_values[i]:.4f}")
