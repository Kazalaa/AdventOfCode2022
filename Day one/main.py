from itertools import groupby
import os

cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, "input.txt")

with open(fichier, 'r') as f:
    # split the data in one list with blanks every line breaks (between two blocks of data):
    full_data = f.read().split('\n')
    # remove the blanks:
    split_data = [list(g) for k, g in groupby(full_data, key=bool) if k]
    first_result = 0
    second_result = []
    for data in split_data:
        data_result = [int(i) for i in data]
        data_result = sum(data_result)
        if data_result > first_result:
            first_result = data_result
        second_result.append(data_result)
    second_result.sort()
    second_result = sum(second_result[-3:])
print(f"--- Day 1: Calorie Counting --- That Elf carrying {first_result} Calories")
print(f"--- Day 1: Calorie Counting --- The top three Elves carrying {second_result} Calories")

