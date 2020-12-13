import numpy as np

# 1.11.2
A = np.matrix("1, -1, 2, 4, 0; 8, 2, 0, 5, 3; 0, 1, 2, 1, 2")
print("A:\n", A)

B = np.matrix("1, 0, 1, 0; 0, 0, 2, -1; 1, 0, 1, 1; 0, 1, 1, 1; 1, 1, 0, -1")
print("B:\n", B)

print("C:\n", np.dot(A, B))

# 1.11.4
a = np.array([1, 3])
b = np.array([-3, 1])
print(np.outer(a, b))
