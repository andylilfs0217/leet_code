import collections
from io import TextIOWrapper
import math
import statistics
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    left_set = set(['(', '{', '[', '<'])
    right_set = set([')', '}', ']', '>'])
    LEFT_RIGHT = {'(': ')', '{': '}', '[': ']', '<': '>'}
    RIGHT_LEFT = {')': '(', '}': '{', ']': '[', '>': '<'}
    POINT_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for line in lines:
        char_stack = []
        for char in line:
            if char in left_set:
                char_stack.append(char)
            elif LEFT_RIGHT[char_stack[-1]] == char:
                char_stack.pop()
            else:
                point = POINT_MAP[char]
                res += point
                break

    # Finish your codes here
    return res
