import random

def rotate_the_barel(num_slots):
    return random.randint(1, num_slots)

def simulate_game_with_rotate(num_games,first,second,num_slots):
    win = 0
    lose = 0
    for _ in range(num_games):
        slot_after_rotate = rotate_the_barel(num_slots)
        slot_after_rotate_1 = slot_after_rotate + 1
        if slot_after_rotate_1 > num_of_slots:
            slot_after_rotate_1 = 1

        if (first == slot_after_rotate) or (second == slot_after_rotate):
            lose += 1
        elif (first == slot_after_rotate_1) or (second == slot_after_rotate_1) :
            lose += 1
        else:
            win += 1

    b = lose/num_games 
    return b

def simulate_game_without_rotate(num_games,first,second,num_slots):
    win = 0
    lose = 0
    for _ in range(num_of_games):
        slot_after_rotete_1 = rotate_the_barel(num_slots)
        if (slot_after_rotete_1 == first) or (slot_after_rotete_1 == second):
            lose += 1
        else:
            slot_after_rotete_2 = rotate_the_barel(num_slots)
            if (slot_after_rotete_2 == first) or (slot_after_rotete_2 == second):
               lose += 1
            else:
               win += 1
    chance = lose/num_games
    return chance

print("Introduce the number of slots")
num_of_slots = int(input())
print("Introduce the number of simulations")
num_of_games = int(input())
print (f"Introduce the place of first bulet from 1 to {num_of_slots}")
first_bulet = int(input())
print(f"Introduce the place of second bulet from 1 to {num_of_slots}, not {first_bulet} ")
second_bulet = int(input())
x = simulate_game_with_rotate(num_of_games,first_bulet,second_bulet,num_of_slots)
y = simulate_game_without_rotate(num_of_games,first_bulet,second_bulet,num_of_slots)
print(f"according to the experiment the chance to lose if you rotate the barel is {x}")
print(f"according to the experiment the chance to lose if you don't rotate the barel is {y}")