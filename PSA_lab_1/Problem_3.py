import random

def calculate_sum(arr):
    return sum(arr)

def simulate_labouchere(bet_list):
    max_loss = 0
    i=1
    while len(bet_list) > 0:
        first_number = bet_list[0]
        last_number = bet_list[-1]
        bet_amount = first_number + last_number if len(bet_list) > 1 else first_number

        a = random.random()
        
        roulette_outcome = 'win' if a>0.5 else 'lose'
        
        if roulette_outcome == 'win':
            bet_list.pop(0)
            bet_list.pop() if len(bet_list) > 0 else None
            print(f"{i}) {bet_list}")
        else:
            bet_list.append(bet_amount)
            max_loss -= bet_amount
            print(f"{i}) {bet_list}")
        i += 1
    print(f"you played {i-1} times")
    return max_loss

initial_list = list(map(int, input("Enter the initial list of numbers separated by space: ").split()))

total_losses = 0
losses = simulate_labouchere(initial_list.copy())
total_losses += losses
total_sum = sum(initial_list)
average_loss = total_losses 
print(f'Before you win {total_sum} you lose {total_losses}')
