import numpy as np

arr = np.array([1, 2, 4, 8, 16])

ln = np.log(arr)
log10 = np.log10(arr)
log2 = np.log2(arr)
exp = np.exp(arr)

print("Array:", arr)
print("Natural log:", ln)
print("Base-10 log:", log10)
print("Base-2 log:", log2)
print("Exponential:", exp)
