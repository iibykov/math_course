import numpy as np

# 1.9.1
A = np.matrix("1, 1; 5, 7")
B = np.matrix("6, 1; -5, 5")
print(A+B)

# 1.9.2
A1 = np.matrix("3, 9; 6, 27")
print(A1/3)

# 1.9.3
R = np.matrix("1, 5, 4; 0, 1, 0")
print('R.T:\n', R.T)
