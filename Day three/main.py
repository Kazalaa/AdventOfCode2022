from itertools import groupby
import os

cur_dir = os.path.dirname(__file__)
file = os.path.join(cur_dir, "input.txt")


def priorities_value(item):
    # Uppercase item types A through Z have priorities 27 through 52.
    if item.isupper():
        return ord(item) - 38
    # Lowercase item types a through z have priorities 1 through 26.
    else:
        return ord(item) - 96


with open(file, 'r') as f:
    full_data = f.read().split('\n')
    priorities = 0
    for data in full_data:
        first_part, second_part = data[:len(data)//2], data[len(data)//2:]
        item_type = ''.join(set(first_part).intersection(second_part))
        if item_type.isupper():
            priorities += priorities_value(item_type)
        else:
            priorities += priorities_value(item_type)
    print(f"The sum of the priorities of those item types is {priorities}")

with open(file, 'r') as f:
    full_data = f.read().split('\n')
    second_priorities = 0
    group_of_three = []
    for data in full_data:
        group_of_three.append(data)
        if len(group_of_three) == 3:
            item_type = ''.join(set.intersection(*map(set, group_of_three)))
            second_priorities += priorities_value(item_type)
            group_of_three.clear()
    print(f"The sum of the priorities of those item types is {second_priorities}")