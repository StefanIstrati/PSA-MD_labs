import random
import math

def simulate_toss_of_coin(nr_simultations):
    total = 0
    k = 0
    for _ in range(nr_simultations):
        x = random.uniform(1,8)
        y = random.uniform(1,8)
        if (int(x + 0.25) != int(x - 0.25)) or (int(y + 0.25) != int(y - 0.25)):
            total -= 0.25
        else: 
            total += 1
            k +=1
    return total/nr_simultations, k/nr_of_simulations

nr_of_simulations = int(input("introduce the number of simulations: "))
probability = []
probability = simulate_toss_of_coin(nr_of_simulations)
if probability[0] < 0.50:
    print(f"this game isn't fair, probability of winning is: {probability[1]}, the average winning is {probability[0]}")
else:
    print(f"this game is fair, probability of winning is: {probability[1]}, the average winning is {probability[0]}")