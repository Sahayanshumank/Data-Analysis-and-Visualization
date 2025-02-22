# c. Test whether the elements of a given 1D array are zero, non-zero and NaN. Record the indices of # these elements in three separate arrays.

import numpy as np

# Sample 1D array
array = np.array([0, 1, np.nan, 2, 0, np.nan, 3, 4, 0])

# Indices of zero elements
zero_indices = np.where(array == 0)[0]

# Indices of non-zero elements
non_zero_indices = np.where(array != 0)[0]

# Indices of NaN elements
nan_indices = np.where(np.isnan(array))[0]

print("Indices of zero elements:", zero_indices)
print("Indices of non-zero elements:", non_zero_indices)
print("Indices of NaN elements:", nan_indices)