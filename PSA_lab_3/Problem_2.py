import random
import math

def simulate_random_point_on_the_target():
    point = random.uniform(0, math.pi)
    x = random.uniform(0,math.cos(point))*10
    y = random.uniform(0,math.sin(point))*10
    return x,y

nr_of_simulations = int(input("Input number of simulations: "))
right_half = 0
distance_less_than_5 = 0
distance_greater_than_5 = 0
exact_5_inches_to_0_5_point = 0
for _ in range(nr_of_simulations):
    x,y = simulate_random_point_on_the_target()
    if x > 0: 
        right_half += 1
    distance = math.sqrt(x**2 + y**2)
    if distance < 5:
        distance_less_than_5 += 1
    else:
        distance_greater_than_5 += 1
    distance = math.sqrt((0-x)**2+(5-y)**2)
    if distance == 5:
        exact_5_inches_to_0_5_point += 1
print(f"The probability that the dart lands in the right part of target is: {right_half/nr_of_simulations}")
print(f"The probability that distance from the center is less than 5 inches is: {distance_less_than_5/nr_of_simulations}")
print(f"The probability that distance from the center is greater than 5 inches is: {distance_greater_than_5/nr_of_simulations}")
print(f"The probability that the distance from point (0,5)in 5 inches is: {exact_5_inches_to_0_5_point/nr_of_simulations}")