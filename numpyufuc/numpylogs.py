
from math import log
import numpy as np
arr = np.arange(1, 10)
arr1 = np.arange(1, 10)
arr3 = np.arange(1, 10)
nplog = np.frompyfunc(log, 2, 1)

print(np.log2(arr))
print(np.log10(arr1))
print(np.log(arr3))
print(nplog(100, 15))