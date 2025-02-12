import random

def simulate_monty_hall(IsPlayerChangedDoor, TestAmount):
    WinNum = 0
    
    for _ in range(TestAmount):
        doors = ["goat", "goat", "car"]
        random.shuffle(doors)
        
        player_choice = random.randint(1, 3) - 1
        
        
        if IsPlayerChangedDoor:
            revealed_door = next(i for i in range(3) if i != player_choice and doors[i] == "goat")
            final_choice = next(i for i in range(3) if i != player_choice and i != revealed_door)
        else:
            final_choice = player_choice
        
        if doors[final_choice] == "car":
            WinNum += 1
    return WinNum

WRC = simulate_monty_hall(True, 100)
print(f"Probability of winning if you change your choice: {WRC}")

WRNC = simulate_monty_hall(False, 100)
print(f"Probability of winning if you do not change your choice: {WRNC}")
