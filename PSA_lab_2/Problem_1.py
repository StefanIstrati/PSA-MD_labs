import random
import matplotlib.pyplot as plt

num_trials = int(input("Enter the number of simulations: "))
i_count = 0
j_count = 0

occurrences_9 = []
occurrences_10 = []

for _ in range(num_trials):
    var1 = random.randint(1, 6)
    var2 = random.randint(1, 6)
    var3 = random.randint(1, 6)

    total = var1 + var2 + var3

    if total == 9:
        i_count += 1
    elif total == 10:
        j_count += 1

    occurrences_9.append(i_count)
    occurrences_10.append(j_count)

plt.plot(range(1, num_trials + 1), [occurrences_9[-1]] * num_trials, label='Sum = 9')
plt.plot(range(1, num_trials + 1), [occurrences_10[-1]] * num_trials, label='Sum = 10')

plt.xlabel('Number of Trials')
plt.ylabel('Occurrences')
plt.title('Final Occurrences of Sum = 9 and Sum = 10')
plt.legend()
plt.show()
