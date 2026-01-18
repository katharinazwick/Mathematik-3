import numpy as np

# Parameter
num_sim = 10000  # Anzahl der Wiederholungen
n = 10
mu0 = 12
mu_true = 10
sigma_true = 5.77
z_crit = 1.96

accept = 0
reject = 0

for _ in range(num_sim):
    # Simulation der Stichprobe
    X = np.random.normal(mu_true, sigma_true, size=n)

    #  Stichprobenmittelwert
    X_bar = np.mean(X)

    #   Stichprobenstandardabweichung (unverzerrt, ddof=1)
    S = np.std(X, ddof=1)

    # t-Teststatistik
    t_stat = (X_bar - mu0) / (S / np.sqrt(n))

    if t_stat < z_crit:
        accept += 1
    else:
        reject += 1

print("accept:", accept,"reject:", reject)
