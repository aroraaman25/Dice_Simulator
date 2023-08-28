import os
os.system("cls")

import random

again = True
while again:
    # first_roll = random.randint(0,6)
    # second_roll = random.randint(0,6)
    # third_roll = random.randint(0,6)
    first_roll=random.randint(1,6)
    print(first_roll) 
    if first_roll == 6:
        second_roll=random.randint(1,6)
        print(second_roll)
        if second_roll == 6:
            third_roll=random.randint(1,6)
            print(third_roll)
            # print(third_roll)
            if third_roll == 6:
                print('Chance Nullified')
            elif(third_roll < 6):
                continue
        else:
            break
    else:
        break