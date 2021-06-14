import numpy as np
new = np.array([10,20,30,40])
print(new)

print(type(new))
second = np.asarray(new, dtype = "float",order = "f")

print(new[2])

for i in np.nditer(new):
   print(i)


new1 = np.array([[15,9,4],[54,41,96]])
print(new1)
print(new1[1][:2])

new3 = np.array([[[12,15,45],[48,46,42],[56,82,66]]])
print(new3)
print(new3[0][2][:2])
new3 = np.array(['manju', 'teja', 'hari'])

