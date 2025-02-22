# a. Compute the mean, standard deviation, and variance of a two dimensional random integer array along the second axis.

import numpy as np

data = np.random.randint(0, 100, (3,5))

print("Data:-↴\n", data)

mean = np.mean(data, axis=1)
std = np.std(data, axis=1)
var = np.var(data, axis=1)

print("Mean: ", mean)
print("Standard Deviation: ", std)
print("Variance: ", var)

