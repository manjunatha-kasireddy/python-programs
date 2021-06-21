import numpy as np
num1 = 4
num2 = 6
arr = np.array([3, 6, 9])
x = np.lcm(num1, num2)
x1 = np.lcm.reduce(arr)
print(x)
print(x1)