import numpy as np

apartment = np.array([59.50, 31.40, 19, 22, 60550, 2])
share_living_space = apartment[1]/apartment[0]
apartment = np.delete(apartment, [0, 1])
apartment = np.append(apartment, share_living_space)

print(share_living_space)
print(apartment.shape)

# temperature
t = np.array([12, 14, 17, 19, 24, 28, 31, 31, 27, 22, 17, 13])
print(t[5])
print(t[1])
