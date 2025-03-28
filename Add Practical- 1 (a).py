import numpy as np
import random

data = np.random.randint(0,100,size=(3,5))

m1 = np.mean(data,0)
m2 = np.std(data,0)
m3 = np.var(data,0)

print("Data \n",data)

print("Mean of Data\n",m1)
print("Standard Deviation of Data\n",m2)
print("Variance of Data\n",m3)
