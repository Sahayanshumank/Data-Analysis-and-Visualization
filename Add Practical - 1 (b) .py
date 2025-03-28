import numpy as np

n = int(input("Enter the No. of Rows: "))
m = int(input("Enter the No. of Column: "))

data = np.random.randint(0,100,size=(m,n))

print("Shape of Data is \n",data)

print("Type of Data is ",type(data))

print("Type of Data is ",data.dtype)

data2 = data.reshape(n,m)

print("Reshape data :\n",data2)