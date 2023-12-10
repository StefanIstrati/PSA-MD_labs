import random

def simulate_waiting_time(average_time_between_occurrences, num_simulations):
    lambda_parameter = 1 / average_time_between_occurrences
    waiting_times = [random.expovariate(lambda_parameter) for _ in range(num_simulations)]
    average_waiting_time = sum(waiting_times) / num_simulations
    return average_waiting_time

average_time = int(input("Nr. of minutes betwen occurrences: "))
num_simulations = int(input("Nr. of simulations: "))
result = simulate_waiting_time(average_time, num_simulations)
print(f"Simulated average waiting time: {result:.2f} minutes")
