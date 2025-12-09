from math import comb
from decimal import Decimal, getcontext

getcontext().prec = 50

n = 300
p = Decimal(1) / Decimal(3)
prob = Decimal(0)
for k in range(81, 120):
    prob += Decimal(comb(n, k)) * (p**k) * ((Decimal(1)-p)**(n-k))

print(float(prob))
