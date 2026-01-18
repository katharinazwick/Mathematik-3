import random
import matplotlib.pyplot as plt

means = []
current_sum = 0

for n in range(1, 100001):
    x = random.uniform(-10000, 10000)
    current_sum += x
    means.append(current_sum / n)

plt.plot(means) #zeichnet Werte
plt.xlabel("n") #Beschriftung
plt.ylabel("X̄_n")
plt.title("Konvergenz des arithmetischen Mittels") #Title
plt.show()
