import collections
from io import TextIOWrapper
import math
import statistics
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    DISPLAY_DIGIT_MAP = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }
    res = 0
    all_patterns, all_outputs = [], []
    for line in lines:
        a, b = line.split(' | ')
        a, b = a.split(), b.split()
        all_patterns.append(a)
        all_outputs.append(b)

    for i, patterns in enumerate(all_patterns):
        len_map = collections.defaultdict(list[str])
        for pattern in patterns:
            len_map[len(pattern)].append(set(pattern))
        a = len_map[3][0] - len_map[2][0]
        f = len_map[2][0] & len_map[6][0] & len_map[6][1] & len_map[6][2]
        c = len_map[2][0] - f
        d = len_map[4][0] & len_map[5][0] & len_map[5][1] & len_map[5][2]
        g = len_map[5][0] & len_map[5][1] & len_map[5][2] - a - d
        b = len_map[6][0] & len_map[6][1] & len_map[6][2] - a - f - g
        e = len_map[7][0] - a - b - c - d - f - g

        wrong_correct_map = {}
        wrong_correct_map[a.pop()] = 'a'
        wrong_correct_map[b.pop()] = 'b'
        wrong_correct_map[c.pop()] = 'c'
        wrong_correct_map[d.pop()] = 'd'
        wrong_correct_map[e.pop()] = 'e'
        wrong_correct_map[f.pop()] = 'f'
        wrong_correct_map[g.pop()] = 'g'

        outputs = all_outputs[i]
        correct_number = ''
        for output in outputs:
            correct_output = ''.join(
                sorted([wrong_correct_map[seg] for seg in output]))
            digit = DISPLAY_DIGIT_MAP[correct_output]
            correct_number += digit
            pass

        res += int(correct_number)

        pass

    # Finish your codes here
    return res
