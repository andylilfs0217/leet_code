from enum import Enum
from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    def charToNum(c: str) -> int:
        number = ord(c)
        if number > 96:
            minus = 96
        else:
            minus = 64 - 26
        number = number - minus
        return number

    res = 0
    n = len(lines)
    for i in range(0, n, 3):
        first, second, third = lines[i:i + 3]
        intersect = set(first) & set(second) & set(third)
        intersect_char = intersect.pop()
        number = charToNum(intersect_char)
        res += number

    # Finish your codes here
    return res
