import numpy as np

array1 = np.random.randint(0,100,size=(10))
array2 = np.random.randint(0,100,size=(10))
array3 = np.random.randint(0,100,size=(10))
print(array1)
print(array2)
print(array3)

array4 = array3-array2

print(array4)

array5 = array1*2
print(array5)

print("Covariancce of \n",np.cov(array1,array4)[0,1])
print("Correlation of \n",np.corrcoef(array1,array4)[0,1])