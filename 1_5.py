import numpy as np

a = np.array([65, 70, 120, 30])
w = np.array([0.4, 0.4, 0.2, 0.8])
print(np.dot(a, w))

# 1.5.2
x = np.array([4, 5, -1])
y = np.array([2, 0, 1])
print(np.dot(x, y))

# 1.5.4
x = np.array([4, 6, 1])
print(np.sqrt(np.dot(x, x)))
