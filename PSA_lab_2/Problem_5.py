import random

def simulate_boy():
    x = ""
    k = 0
    list = ["G","B"]
    while x != "B":
        x = random.choice(list)
        k +=1
    return k
def simulate_at_leas_one_boy_and_at_leas_one_girl():
    x = ""
    k = 0
    list = ["G","B"]
    while (x != "B")or(x != "B"):
        x = random.choice(list)
        k +=1
    return k
nr_simulations = int(input("introduce the number of families: "))
total = 0
for _ in range(nr_simulations):
    total += simulate_boy()
print(f"the average number of children if family had a children until a boy is {total/nr_simulations}")

total = 0

for _ in range(nr_simulations):
    total += simulate_at_leas_one_boy_and_at_leas_one_girl()
print(f"the average number of children if family had at least one boy and at least one girl {total/nr_simulations}")