import random

def simulate_elections(percent_rep, percent_dem, nr_voters, nr_simulations):
    list = ["1","0"]
    vote_for_rep = 0
    for _ in range(nr_simulations):
        k = 0
        for _ in range(nr_voters):
            i = random.choices(list, weights = [percent_dem,percent_rep], k = 1)
            if i == "0":
                k += 1
        if k > nr_voters - k:
            vote_for_rep += 1
    return vote_for_rep

percent_rep = float(input("introduce the percentage for republican candidate: "))
percent_dem = float(input("introduce the percentage for democratic candidate: ")) 
voters = int(input("introduce the number of voters for the poll: "))

winner = simulate_elections(percent_rep,percent_dem, voters, 100)

if winner > 50:
    print(f"after 100 simulations with percentages {percent_rep}/{percent_dem}, the Republican candidate wins")
else:
    print(f"after 100 simulations with percentages {percent_rep}/{percent_dem}, the Democratic candidate wins")

