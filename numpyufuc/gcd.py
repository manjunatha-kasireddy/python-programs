import numpy as np
arr = np.array([20, 8, 32, 36, 16])
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
x1 = np.gcd.reduce(arr)

print(x)
print(x1)
