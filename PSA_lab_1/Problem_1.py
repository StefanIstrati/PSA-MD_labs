import random
import matplotlib.pyplot as plt

def flip_coin_until_head():
    flips = 1
    while random.randint(0, 1) == 0:  
        flips += 1
    return flips

def simulate_games(num_games):
    total_winnings = 0
    for _ in range(num_games):
        flips = flip_coin_until_head()
        winnings = 2**flips
        total_winnings += winnings
    return total_winnings / num_games

num_simulations = int(input("Enter the number of simulations: "))
average_winnings_list = []

for _ in range(10):
    average_winnings = simulate_games(num_simulations)
    average_winnings_list.append(average_winnings)
    print(average_winnings)

plt.plot(range(1, 11), average_winnings_list, marker='o')
plt.xlabel('Simulation Number')
plt.ylabel('Average Winnings')
plt.title('Average Winnings in 10 Simulations')
plt.show()
