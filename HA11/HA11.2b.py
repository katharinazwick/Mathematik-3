import numpy as np

# Reproduzierbarkeit
np.random.seed(42)

# Anzahl Beobachtungen
n = 10

# Realisierung von X und Z
X = np.random.uniform(0, 1, n)
Z = np.random.uniform(-100, 100, n)

# Y berechnen
Y = 0.5 * X + Z

# Lineare Regression (kleinste Quadrate)
X_mat = np.column_stack((np.ones(n), X))  # Designmatrix [1, X] weil Y=Xmat⋅β+ϵ
beta_hat = np.linalg.inv(X_mat.T @ X_mat) @ X_mat.T @ Y #kleinste Quadratlösung β = (X^T X) ^-1 X^T Y
beta_0, beta_1 = beta_hat #βhat = β0 β1 (Matrix)

print("X:", X)
print("Y:", Y)
print(f"Intercept (β0): {beta_0:.4f}")
print(f"Anstieg (β1): {beta_1:.4f}")
