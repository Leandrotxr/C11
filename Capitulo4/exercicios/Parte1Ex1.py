import numpy as np

arr1 = (np.ones(8).astype(int))
arr2 = np.random.randint(0,10,8)

arr3 = arr1 + arr2

if np.sum(arr3) >= 40:
    print(np.reshape(arr3, (4,2)))
else:
    print(np.reshape(arr3, (2,4)))