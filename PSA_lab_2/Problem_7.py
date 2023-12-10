import random
import matplotlib.pyplot as plt

def simulate_experiment():
    total = 0
    for _ in range(100):
        x = random.choice(["H", "T"])
        if x == "H":
            total += 1
    return total

nr_of_simulations = int(input("introduce number of simulations: "))
result_list = []

for _ in range(nr_of_simulations):
    result_list.append(simulate_experiment())
result_list.sort()

plt.bar(range(1, nr_of_simulations + 1), result_list, color='blue')
plt.xlabel('Simulation Number')
plt.ylabel('Number of Heads')
plt.title('Simulation Results')
plt.show()
