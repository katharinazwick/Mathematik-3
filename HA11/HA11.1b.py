import numpy as np
import matplotlib.pyplot as plt

# Daten
x = np.array([-2, -1, 3, 4, 6])
y = np.array([0, 0.5, 2, 2, 5])

# Regressionsparameter
beta_0 = 0.834
beta_1 = 0.533

# Regressionsgerade
x_line = np.linspace(min(x) - 1, max(x) + 1, 100)
y_line = beta_0 + beta_1 * x_line

# Vorhergesagte Werte
y_hat = beta_0 + beta_1 * x

# Plot
plt.figure()
plt.scatter(x, y)
plt.plot(x_line, y_line)

# Residuen
for xi, yi, yhi in zip(x, y, y_hat):
    plt.plot([xi, xi], [yi, yhi], linestyle='--')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Streudiagramm mit Regressionsgerade und Residuen")
plt.show()
