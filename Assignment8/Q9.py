import numpy as np

def normalize_3d_array():
    data = np.random.rand(4, 3, 2)
    print("Original Array:\n", data)

    for axis in range(3):
        data = (data - data.mean(axis=axis, keepdims=True)) / data.std(axis=axis, keepdims=True)

    return data

normalized_array = normalize_3d_array()
print("\nNormalized Array:\n", normalized_array)