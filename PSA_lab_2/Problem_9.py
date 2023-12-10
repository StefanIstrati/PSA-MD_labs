import random

def simulate_experiment(length_of_sequence, nr_of_sim):
    total = 0
    list = []

    # Generate and sort the sequence
    for _ in range(length_of_sequence):
        list.append(random.random())
    list.sort()

    # Simulate experiments
    for _ in range(nr_of_sim):
        x = random.random()
        for i in range(length_of_sequence):
            if list[i] > x:
                total += i - 1
                break  

    return total / nr_of_sim

length_of_sequence = int(input("Introduce the length of sequence: "))
nr_of_simulations = int(input("Introduce the number of simulations: "))
average_winning = simulate_experiment(length_of_sequence, nr_of_simulations)
print(f"The average winning is: {average_winning}")
