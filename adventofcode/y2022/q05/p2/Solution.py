import collections
from enum import Enum
from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = []
    line_idx = 0
    num_cranes = (len(lines[0]) + 1) // 4
    crane_stacks = [[] for _ in range(num_cranes)]
    while line_idx < len(lines) and lines[line_idx] != '':
        line = lines[line_idx]
        for j in range(0, len(line) + 1, 4):
            char = line[j + 1:j + 2]
            if char != ' ':
                crane_stacks[j // 4].append(char)
        line_idx += 1
    line_idx += 1

    crane_numbers = []
    for i, crane_stack in enumerate(crane_stacks):
        crane_number = crane_stack.pop()
        crane_numbers.append(crane_number)
        crane_stacks[i] = crane_stack[::-1]

    crane_map = collections.defaultdict(list[str])
    for i in range(num_cranes):
        crane_number, crane_stack = crane_numbers[i], crane_stacks[i]
        crane_map[crane_number] = crane_stack

    for line_idx in range(line_idx, len(lines)):
        line = lines[line_idx]
        splits = line.split()
        move_cranes, from_crane, to_crane = int(
            splits[1]), splits[3], splits[5]
        cranes = crane_map[from_crane][-move_cranes:]
        crane_map[to_crane] += cranes
        crane_map[from_crane] = crane_map[from_crane][:-move_cranes]

    for crane_number in crane_numbers:
        crane = crane_map[crane_number][-1]
        res.append(crane)

    res = ''.join(res)

    # Finish your codes here
    return res
