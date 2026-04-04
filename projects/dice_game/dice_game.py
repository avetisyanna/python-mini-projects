import random

def roll_dice():
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    total = r1 + r2
    print(f"Rolled a {total}") 
    return total
    
def game_func():
    first_roll = roll_dice()

    if first_roll in [7, 11]:
        print("You win")
    elif first_roll in [2, 3, 12]:
        print("Casino wins")
    else:
        # This part handles the goal number (4, 5, 6, 8, 9, or 10)
        is_on_and_on = True
        while is_on_and_on == True:
            current_roll = roll_dice()

            if current_roll == first_roll:
                print("You win")
                is_on_and_on = False
            elif current_roll == 7:
                print("Casino wins")
                is_on_and_on = False
            else:
                print("Roll again")

game_func()