import numpy as np

arr = np.array([0,1,2,3,np.nan,4,5,6,np.nan,7,8,0])

print(np.where(arr==0))
print(np.where(arr!=0))
print(np.isnan(arr))