import numpy as np

loss = [-750, - 250]
profit = [100] * 18
print(profit)

cf = loss + profit
print(cf)

print(len(cf))

cashflow = np.array(cf)
npv = np.npv(0.045, cashflow)
print(npv)

irr = np.irr(cashflow)
print(irr)
