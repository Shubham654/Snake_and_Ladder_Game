import random

ladder ={4:56, 22:72, 41:95}
snake ={48:6, 94:50, 75:10}
pos1 = 0

def move(pos):
    dice=random.randint(1,6)
    print(f"Dice:{dice}")
    temp_pos = pos
    pos = pos + dice
    if pos in snake:
       print("Bitten by snake")
       pos = snake[pos]
       print(f"Position:{pos}")
    elif pos in ladder:
        print("Climbed by ladder")
        pos = ladder[pos]
        print(f"Position:{pos}")
    elif pos > 100:
        print("Invalid move try again.")
        pos = temp_pos
        print(f"Position:{pos}")
    else:
        print(f"Position:{pos}")
    print("\n")
    return pos

while True:
    A = input("Press \"ENTER\" to throw dice ")
    pos1 = move(pos1)
    if pos1 == 100:
        print("Cobratulations you WON!")
        break
