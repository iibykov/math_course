import numpy as np

a = np.array([10, 8, 5, 1])
b = np.array([5, 15, 9, 7])

print(a + b)
print(a - b)

omega = 0.2
print(omega * b)

# 1.3.1
x = np.array([1, 2, np.sqrt(3)])
y = np.array([-1, -2, 0])
print(x + y)

# 1.3.2
x = np.array([5, 2])
y = np.array([-5, -11])
print(x + y)
print(x - y)

# 1.3.3
alexey = np.array([120, 150, 90])
wife = np.array([130, 130, 130])
mother = np.array([2, 3, 2.5])
eurToRub = 72;

print(eurToRub*mother)
print(eurToRub*mother + alexey + wife)
