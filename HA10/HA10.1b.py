import numpy as np

# Setze Zufallsseed für Reproduzierbarkeit
np.random.seed(42)

# Parameter
n = 10
mu0 = 12
sigma2 = 100/3
sigma = np.sqrt(sigma2)
z_crit = 1.96

# Simulation der Stichprobe
X = np.random.uniform(0, 20, size=n)

# Stichprobenmittelwert
X_bar = np.mean(X)

# Standardisierte Teststatistik
Z = (X_bar - mu0) / np.sqrt(sigma2 / n)

print(X, X_bar, Z)
print(Z, Z <= z_crit)

