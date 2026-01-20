import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Daten generieren
np.random.seed(42)
n = 100
X = np.random.uniform(0, 10, n)
Z = np.random.uniform(-10, 10, n)
Y = 0.5 * X**0.7 + 0.1 * (X - 20)**2 + Z

# 2. Features erzeugen
X1 = X**2
X2 = X**0.5
X3 = np.log(X + 1e-6)
X_features = np.column_stack((X1, X2, X3))

# 3. Regression fitten
reg = LinearRegression()
reg.fit(X_features, Y)  # Jetzt ist reg korrekt eine Instanz von LinearRegression

# 4. Neue Realisierung
X_new = np.random.uniform(0, 10)
Z_new = np.random.uniform(-10, 10)
Y_new = 0.5 * X_new**0.7 + 0.1 * (X_new - 20)**2 + Z_new

# 5. Neue Features
X1_new = X_new**2
X2_new = X_new**0.5
X3_new = np.log(X_new + 1e-6)
X_new_features = np.array([[X1_new, X2_new, X3_new]])

# 6. Vorhersage
Y_new_hat = reg.predict(X_new_features)

print("X_new:", X_new)
print("Y_new (real):", Y_new)
print("Y_new (predicted):", Y_new_hat[0])
print("Vorhersagefehler:", Y_new - Y_new_hat[0])
