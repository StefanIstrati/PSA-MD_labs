import random

def simulate_experiment(nr_sim):
    list =  ["0", "1", "2"]
    final = 0
    for _ in range(nr_sim):
        nr_of_caught = 0
        total = 0
        for _ in range(730):
            x = random.choices(list,weights=[0.93, 0.5, 0.2],k = 1)[0]
            if x == "1" and nr_of_caught == 0 :
                total += 50
                nr_of_caught +=1
            elif x == "1" and nr_of_caught == 1 :
                total += 200
                nr_of_caught += 1
            elif  x == "1" and nr_of_caught > 1 :
                total +=300
                nr_of_caught += 1
            if x == 2:
                total += 6
        final += total
    return final/nr_sim

number_of_simulations = int(input("introduce the number of simulations: "))
expected_coast = simulate_experiment(number_of_simulations)
print(f"The expected coast of riding troleibuz one year(two times a day) without paying is: {expected_coast}")
real_coast = 2*365*6
if expected_coast < real_coast:
    print("expected value is less than coast paid by us")
else:
    print("expected value is greater than coast paid by us")

        