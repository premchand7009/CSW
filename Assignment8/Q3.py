import numpy as np
import random
import time

# -------- NumPy method --------
start_np = time.time()
arr_np = np.random.random((1000, 1000))
end_np = time.time()

np_time = end_np - start_np
print("NumPy array generation time:", np_time, "seconds")

# -------- Python nested loop method --------
start_py = time.time()

arr_py = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(random.random())
    arr_py.append(row)

end_py = time.time()

py_time = end_py - start_py
print("Python nested loop generation time:", py_time, "seconds")

# -------- Comparison --------
if np_time < py_time:
    print("NumPy method is faster")
else:
    print("Python nested loop method is faster")

