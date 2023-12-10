import random
import matplotlib.pyplot as plt

def simulate_martingale():
    initial_bet = 1
    max_loss = 100
    target_win = 5

    total_winnings = 0
    total_losses = 0

    for _ in range(num_simulations):
        current_bet = initial_bet
        current_winnings = 0
        current_loss = 0

        while current_winnings < target_win and current_loss < max_loss:
            roulette_outcome = random.choice(['win', 'lose'])

            if roulette_outcome == 'win':
                current_winnings += current_bet
                current_bet = initial_bet
            else:
                current_loss += current_bet
                current_bet *= 2

        total_winnings += current_winnings
        total_losses += current_loss

    average_winnings = total_winnings / num_simulations
    average_losses = total_losses / num_simulations

    return average_winnings, average_losses


num_simulations = int(input("Enter the number of simulations: "))

avg_winnings_list = []
avg_losses_list = []

for _ in range(10): 
    avg_winnings, avg_losses = simulate_martingale()
    avg_winnings_list.append(avg_winnings)
    avg_losses_list.append(avg_losses)

plt.plot(avg_winnings_list, label='Average Winnings')
plt.plot(avg_losses_list, label='Average Losses')
plt.xlabel('Simulation')
plt.ylabel('Amount')
plt.title('Martingale System Simulation Results')
plt.legend()
plt.show()
