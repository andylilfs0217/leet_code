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
    for line in lines:
        n = len(line)
        first, second = set(line[:n // 2]), set(line[n // 2:])
        union = first & second
        union_char = union.pop()
        number = charToNum(union_char)
        print(number)
        res += number

    # Finish your codes here
    return res
