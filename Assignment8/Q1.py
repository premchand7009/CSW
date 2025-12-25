import numpy as np
v1 = np.random.randint(1,100,size=10)
print("Vector v1:",v1)
max_val = np.max(v1)
min_val = np.min(v1)
print("Maximum value in v1:", max_val)
print("Minimum value in v1:", min_val)
count_betn = np.sum((v1 > min_val) & (v1 < max_val))
print("Number of elements between max and min:", count_betn)