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
    POINT_MAP = {')': 1, ']': 2, '}': 3, '>': 4}
    points = []
    for line in lines:
        char_stack = []
        for char in line:
            if char in left_set:
                char_stack.append(char)
            elif LEFT_RIGHT[char_stack[-1]] == char:
                char_stack.pop()
            else:
                char_stack = []
                break
        if len(char_stack) > 0:
            point = 0
            while char_stack:
                left_char = char_stack.pop()
                point *= 5
                right_char = LEFT_RIGHT[left_char]
                point += POINT_MAP[right_char]
            points.append(point)
    res = statistics.median(points)

    # Finish your codes here
    return res
