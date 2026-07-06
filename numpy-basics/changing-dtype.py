import numpy as np

arr = np.array([1,2,3])

print(type(arr))
print(arr.dtype)


print(arr.astype(np.float64))


arr1 = arr.astype(np.float64)

print(arr1.dtype)

