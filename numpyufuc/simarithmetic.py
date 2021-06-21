import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

new = np.add(arr1, arr2)
newa = np.subtract(arr1, arr2)
newar = np.multiply(arr1, arr2)
newarr = np.divide(arr1, arr2)
newarr1 = np.power(arr1, arr2)

print(new)
print(newa)
print(newar)
print(newarr)
print(newarr1)