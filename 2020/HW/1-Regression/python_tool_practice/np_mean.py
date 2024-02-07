# numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)

import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
mean_1d = np.mean(arr_1d)
print("Mean of 1D array:", mean_1d)

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
mean_2d_col = np.mean(arr_2d, axis=0)  # Mean along columns
mean_2d_row = np.mean(arr_2d, axis=1)  # Mean along rows
print("Mean along columns:", mean_2d_col)
print("Mean along rows:", mean_2d_row)

print(type(mean_1d))
print(type(mean_2d_col))
print(type(mean_2d_row))
