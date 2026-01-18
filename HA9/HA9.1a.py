import numpy as np

m = 10_000
interval = (9,11)

def simulate(n):
    count = 0
    for _ in range(m):
        sample = np.random.uniform(0, 20, n)
        Tn = sample.mean()
        if interval[0] <= Tn <= interval[1]:
            count += 1
    return count / m

for n in [1, 10, 100]:
    print(f"n = {n}: {simulate(n):.4f}")

