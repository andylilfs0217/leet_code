import collections
from io import TextIOWrapper
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    def getSteps(from_coor: List[int], to_coor: List[int]) -> List[List[int]]:
        steps = []
        from_coor, to_coor = sorted([from_coor, to_coor])
        if from_coor[1] == to_coor[1]:
            for i in range(to_coor[0] - from_coor[0] + 1):
                steps.append((from_coor[0] + i, from_coor[1]))
        elif from_coor[0] == to_coor[0]:
            for i in range(to_coor[1] - from_coor[1] + 1):
                steps.append((from_coor[0], from_coor[1] + i))
        return steps

    def coorToStr(coor: List[int]) -> str:
        return ','.join(map(str, coor))

    res = 0
    moves = []
    all_steps = collections.defaultdict(int)
    for line in lines:
        from_coor, to_coor = line.split(' -> ')
        from_coor = tuple(map(int, from_coor.split(',')))
        to_coor = tuple(map(int, to_coor.split(',')))
        if from_coor[0] == to_coor[0] or from_coor[1] == to_coor[1]:
            moves.append((from_coor, to_coor))

    for from_coor, to_coor in moves:
        steps = getSteps(from_coor, to_coor)
        for step in steps:
            step_str = coorToStr(step)
            all_steps[step_str] += 1

    for count in all_steps.values():
        if count > 1:
            res += 1

    # Finish your codes here
    return res
