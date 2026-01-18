import numpy as np
from scipy.stats import rankdata

# optional: Seed für Reproduzierbarkeit
np.random.seed(42)

# Stichprobengrößen
n = 10
m = 20
z_crit = 1.96

# Simulation der Stichproben
X = np.random.uniform(0, 20, size=n)
Y = np.random.uniform(5, 16, size=m)

# Gemeinsame Stichprobe
Z = np.concatenate([X, Y])

# Ränge berechnen
ranks = rankdata(Z)

# Rangsumme der X-Stichprobe = Teststatistik W
W = np.sum(ranks[:n])

EW = n * (n + m + 1) / 2
VarW = n * m * (n + m + 1) / 12

W_std = (W - EW) / np.sqrt(VarW)
    
print(X, Y, W)
print(W_std, W_std <= z_crit)
