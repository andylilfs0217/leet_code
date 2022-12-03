import collections
from io import TextIOWrapper
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    DAYS = 256
    LIFE_CYCLE = 6
    NEW_LIFE_CYCLE = LIFE_CYCLE + 2
    res = 0
    counter = collections.Counter(map(int, lines[0].split(',')))

    for day in range(DAYS):
        new_counter = collections.Counter()
        for life, count in counter.items():
            if life > 0:
                new_life = life - 1
            else:
                new_life = LIFE_CYCLE
                new_counter[NEW_LIFE_CYCLE] += count
            new_counter[new_life] += count

        counter = new_counter

    res = sum(counter.values())

    # Finish your codes here
    return res
