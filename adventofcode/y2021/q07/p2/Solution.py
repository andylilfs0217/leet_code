import collections
from io import TextIOWrapper
import math
import statistics
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = float('inf')
    hposs = list(map(int, lines[0].split(',')))
    hposs_counter = collections.Counter(hposs)
    min_pos, max_pos = min(hposs), max(hposs)
    for pos in range(min_pos, max_pos + 1):
        fuel = 0
        for k, count in hposs_counter.items():
            diff = abs(k - pos)
            fuel += count * ((diff + 1) * diff // 2)
        res = min(res, fuel)

    # Finish your codes here
    return res
