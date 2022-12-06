import os


def contains(section):
    split_section = section.split(",")
    (s1, s2) = (split_section[0].split("-"))
    (s3, s4) = (split_section[1].split("-"))
    if \
            (int(s1) <= int(s3) and int(s2) >= int(s4)) \
            or (int(s1) >= int(s3) and int(s2) <= int(s4)):
        return True
    return False


def overlap(section):
    split_section = section.split(",")
    (s1, s2) = (split_section[0].split("-"))
    (s3, s4) = (split_section[1].split("-"))
    if \
            (int(s1) in range(int(s3), int(s4) + 1))\
            or (int(s2) in range(int(s3), int(s4) + 1)) \
            or (int(s3) in range(int(s1), int(s2) + 1)) \
            or (int(s4) in range(int(s1), int(s2) + 1)):
        return True
    return False


cur_dir = os.path.dirname(__file__)
file = os.path.join(cur_dir, "input.txt")

with open(file, 'r') as f:
    lines = f.readlines()
    result = 0
    overlap_result = 0
    for line in lines:
        if contains(line):
            result += 1
        if overlap(line):
            overlap_result += 1
print(f"In how many assignment pairs does one range fully contain the other ? It's fully contain in {result} pairs")
print(f"In how many assignment pairs do the ranges overlap ? It's overlap in {overlap_result} pairs")
