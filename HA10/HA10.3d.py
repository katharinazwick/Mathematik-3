import numpy as np
from scipy.stats import rankdata

# Parameter
num_sim = 1000
n = 10
m = 20
z_crit = 1.96

accept = 0
reject = 0

for _ in range(num_sim):
    X = np.random.uniform(0, 20, size=n)
    Y = np.random.uniform(0, 20, size=m)

    Z = np.concatenate([X, Y])
    ranks = rankdata(Z)

    W = np.sum(ranks[:n])

    EW = n * (n + m + 1) / 2
    VarW = n * m * (n + m + 1) / 12

    W_std = (W - EW) / np.sqrt(VarW)

    if abs(W_std) <= z_crit:
        accept += 1
    else:
        reject += 1

print("accept:",accept, "reject:",reject)
