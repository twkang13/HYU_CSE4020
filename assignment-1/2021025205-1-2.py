import numpy as np

M = np.arange(2, 27)
print(M)
print()

M = np.reshape(M, (5,5))
print(M)
print()

for i in range(5):
    M[i][0] = 0
print(M)
print()

M = M @ M
print(M)
print()

v = np.array(M)
v = v[0:1, 0:5]

timeSum = 0
for i in range(5):
    timeSum += v[0,i] * v[0,i]
print(np.sqrt(timeSum))