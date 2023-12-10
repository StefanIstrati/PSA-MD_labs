import random

def simulate_triangle():
    
    a = random.uniform(0, 1)
    b = 1 - a

    if a > b:
        c = random.uniform(0, a)
        a -= c
    else:
        c = random.uniform(0, b) 
        b -= c

    if (a + b > c) and (a + c > b) and (b + c > a):
        return 1
    else:
        return 0

nr_of_simulations = int(input("Input number of simulations: "))

possible = 0
for _ in range(nr_of_simulations):
    result = simulate_triangle()
    possible += result

probability = possible / nr_of_simulations
print(f"The probability that the three pieces can be used to form a triangle is: {probability}")
