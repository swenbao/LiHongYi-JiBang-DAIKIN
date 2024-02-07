# numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)

import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
std_1d = np.std(arr_1d)
print("Standard deviation of 1D array:", std_1d)

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
std_2d_col = np.std(arr_2d, axis=0)  # Standard deviation along columns
std_2d_row = np.std(arr_2d, axis=1)  # Standard deviation along rows
print("Standard deviation along columns:", std_2d_col)
print("Standard deviation along rows:", std_2d_row)

print(type(std_1d))
print(type(std_2d_col))
print(type(std_2d_row))