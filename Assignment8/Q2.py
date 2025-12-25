import numpy as np

v1 = np.random.randint(1, 10, size=2)
v2 = np.random.randint(1, 10, size=2)

print("Vector v1:", v1)
print("Vector v2:", v2)

len_v1 = np.linalg.norm(v1)
len_v2 = np.linalg.norm(v2)

print("Length of v1 vector:", len_v1)
print("Length of v2 vector:", len_v2)

v1Norm = v1 / len_v1
v2Norm = v2 / len_v2

print("Normalized v1:", v1Norm)
print("Normalized v2:", v2Norm)

dot = np.dot(v1, v2)
cos_theta = dot / (len_v1 * len_v2)

angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

print("Angle between v1 and v2 in radians:", angle_rad)
print("Angle between v1 and v2 in degrees:", angle_deg)
