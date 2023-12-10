import random

def simulate_seating(n,nr_simulations):
    for _ in range(nr_simulations):

        seating = list(range(n))
        random.shuffle(seating)
        valid_seating = all(seating[i] != seating[(i + 1) % n] and seating[i] != seating[(i - 1) % n] for i in range(n))
        if valid_seating:
            return 1
        
    return 0
  
n = int(input("inroduce the number of participants: "))
nr_simulate = int(input("introudce the number of simulations"))
probability = simulate_seating(n,nr_simulate) / nr_simulate 

print(f"Estimated probability for {n} participants: {probability}")
