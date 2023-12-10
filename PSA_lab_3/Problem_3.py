import random 

list = []
for i in range(100):
    list.append(i+1)
k = 0
last_place = random.choice(list)
simulations = int(input("Input the number of simulations: "))
for _ in range(simulations):
    list = []
    for i in range(100):
        list.append(i+1)
    for _ in range(1,99):
        x = random.choice(list)
        list.remove(x)
    if list[0] == last_place:
        k += 1

print(f"probability that the last person takes his assigned seat is: {k/simulations}")