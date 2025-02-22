# b. Create a 2-dimensional array of size m x n integer elements, also print the shape, type and data type of the array and then reshape it into an n x m array, where n and m are user inputs given at the run time.


import numpy as np

# Get user inputs for dimensions
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Create a 2-dimensional array of size m x n with random integers
array = np.random.randint(1, 100, size=(m, n))

# Print the shape, type, and data type of the array
print("Original array:")
print(array)
print("Shape:", array.shape)
print("Type:", type(array))
print("Data type:", array.dtype)

# Reshape the array into n x m
reshaped_array = array.reshape(n, m)

# Print the reshaped array
print("\nReshaped array:")
print(reshaped_array)
print("Shape:", reshaped_array.shape)
