# d. Create three random arrays of the same size: Array1, Array2 and Array3. Subtract Array 2 from Array3 and store in Array4. Create another array Array5 having two times the values in Array1. Find Covariance and Correlation of Array1 with Array4 and Array5 respectivel

import numpy as np
# Set the size of the arrays
size = 10

# Create three random arrays of the same size
Array1 = np.random.rand(size)
Array2 = np.random.rand(size)
Array3 = np.random.rand(size)

# Subtract Array2 from Array3 and store in Array4
Array4 = Array3 - Array2

# Create another array Array5 having two times the values in Array1
Array5 = 2 * Array1

# Find Covariance of Array1 with Array4
covariance = np.cov(Array1, Array4)[0, 1]

# Find Correlation of Array1 with Array5
correlation = np.corrcoef(Array1, Array5)[0, 1]

print("Array1:-↴\n", Array1)
print("Array2:-↴\n", Array2)
print("Array3:-↴\n", Array3)
print("Array4:-↴\n", Array4)
print("Array5:-↴\n", Array5)
print("Covariance between Array1 and Array4:", covariance)
print("Correlation between Array1 and Array5:", correlation)