import numpy as np

np.random.seed(42)  # für Reproduzierbarkeit

n = 100

# Xi aus U(0,10)
X = np.random.uniform(0, 10, n)

# Zi aus U(-10,10)
Z = np.random.uniform(-10, 10, n)

# Yi berechnen
Y = 0.5 * X**0.7 + 0.1 * (X - 20)**2 + Z


X1 = X**2 #X^2 für lineare Regression da Y nicht linear von X
X2 = X**0.5
X3 = np.log(X + 1e-6)

#Y = beta0 + beta1 X1 + beta2 X2 + beta3 X3 + e
from sklearn.linear_model import LinearRegression

# Features zusammenfügen
X_features = np.column_stack((X1, X2, X3))

# Regression
reg = LinearRegression()
reg.fit(X_features, Y)

# Koeffizienten und Intercept
beta0 = reg.intercept_
betas = reg.coef_

print("Intercept β0:", beta0)
print("Koeffizienten β1, β2, β3:", betas)

############
#Y = 1/2 sum Yi & (Yi - Y)^2
Y_mean = np.mean(Y)
SST = np.sum((Y - Y_mean)**2)
print("Summe der quadratischen Abstände zum Mittelwert (SST):", SST)

#Yi = beta0 + beta1 X1 + beta2 X2 + beta3 X3
Y_hat = reg.predict(X_features)

SSE = np.sum((Y - Y_hat)**2)
print("Summe der quadratischen Abstände zu den gefitteten Werten (SSE):", SSE)

#bestimmheitsmaß R^2 = 1 - SEE / SST
R2 = 1 - SSE / SST
print("R²:", R2)