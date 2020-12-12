import numpy as np

Husband_Income = np.array([100, 220, 140])
Wife_Income = np.array([150, 200, 130])
Mother_In_Law_Income = np.array([90, 80, 100])

Husband_Consumption = np.array([50, 50, 60])
Wife_Consumption = np.array([100, 80, 140])
Mother_In_Law_Consumption = np.array([100, 20, 140])

# 1.10.1
Income = np.array([Husband_Income, Wife_Income, Mother_In_Law_Income])
print("Income.T:\n", Income.T)

# 1.10.2
Consumption = np.array([Husband_Consumption, Wife_Consumption, Mother_In_Law_Consumption])
print("Consumption.T:\n", Consumption.T)

# 1.10.3
Inc_After_Taxes = 0.87*Income.T
print("Income.T after taxes:\n", Inc_After_Taxes)

# 1.10.4
print("Income.T - Consumption.T:\n", Inc_After_Taxes - Consumption.T)
