from itertools import groupby
import os

cur_dir = os.path.dirname(__file__)
file = os.path.join(cur_dir, "input.txt")


def strategy(your_choice):
    if your_choice == "X":
        return 1
    elif your_choice == "Y":
        return 2
    else:
        return 3


with open(file, 'r') as f:
    # split the data in one list:
    full_data = f.read().split('\n')
    first_score = 0
    second_score = 0
    win = ["AY", "BZ", "CX"]
    draw = ["AX", "BY", "CZ"]
    second_strategy = \
        {"AX": 3,
         "BX": 1,
         "CX": 2,
         "AY": 4,
         "BY": 5,
         "CY": 6,
         "AZ": 8,
         "BZ": 9,
         "CZ": 7,
         }
    for line in full_data:
        #  remove blanks between letters
        line = line.replace(" ", "")
        first_score += strategy(line[1])
        if line in win:
            first_score += 6
        elif line in draw:
            first_score += 3
        second_score += second_strategy[line]
    print(f"Your total score according to your strategy guide is {first_score}")
    print(
        f"After correctly decrypting the ultra top secret strategy guide, your total score according to your strategy "
        f"guide is {second_score}") 
