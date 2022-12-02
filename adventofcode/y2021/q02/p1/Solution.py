from io import TextIOWrapper
import math


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    mapper = {
        'up': (0, -1),
        'down': (0, 1),
        'forward': (1, 0),
    }
    pos = (0, 0)  # x, y
    depth = 0
    for line in lines:
        action, distance = line.split(' ')
        distance = int(distance)
        action_map = mapper[action]
        action_map = [num * distance for num in action_map]
        pos = [sum(i) for i in zip(pos, action_map)]
        if action == 'forward':
            depth += pos[1] * distance
        pass

    res = math.prod((pos[0], depth))

    # Finish your codes here
    return res
