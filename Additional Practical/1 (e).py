# e. Create two random arrays of the same size 10: Array1, and Array2. Find the sum of the first half of both the arrays and product of the second half of both the arrays.

import numpy as np

# Create two random arrays of size 10
array1 = np.random.rand(10)
array2 = np.random.rand(10)

# Calculate the sum of the first half of both arrays
sum_first_half = np.sum(array1[:5]) + np.sum(array2[:5])

# Calculate the product of the second half of both arrays
product_second_half = np.prod(array1[5:]) * np.prod(array2[5:])

print("Array1:-↴\n", array1)
print("Array2:-↴\n", array2)
print("\nSum of the first half of both arrays:", sum_first_half)
print("\nProduct of the second half of both arrays:", product_second_half)