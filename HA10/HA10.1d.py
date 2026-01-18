import numpy as np

# Parameter
num_sim = 10000      # Anzahl der Wiederholungen
n = 10               # Stichprobengröße
mu0 =12
sigma2 = 100 / 3
z_crit = 1.96

accept = 0
reject = 0

for _ in range(num_sim):
    # Neue Stichprobe
    X = np.random.uniform(0, 20, size=n)
    X_bar = np.mean(X)

    # Z-Teststatistik
    Z = (X_bar - mu0) / np.sqrt(sigma2 / n)

    # Entscheidungsregel (zweiseitig!)
    if abs(Z) <= z_crit:
        accept += 1
    else:
        reject += 1

print("accept:", accept,"reject:", reject)
